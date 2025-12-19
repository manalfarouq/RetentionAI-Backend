# routes/prediction.py
from fastapi import APIRouter, HTTPException, Depends
from ..schemas.PredictRequest_schema import PredictRequest
from ..db.db_connection import SessionLocal
from ..models.employee import Employee
from ..models.history import History
from ..auth.token_auth import get_current_user
import joblib
import pandas as pd

from app.services.gemini_retention_service import generer_plan_retention

router = APIRouter()

# Charger le modèle ML une seule fois
loaded_model = joblib.load("app/services/modele_attrition_best.pkl")


@router.post("/predict")
def predict(request: PredictRequest, user_id: int = Depends(get_current_user)):

    db = SessionLocal()

    try:
        # 1. Convertir la requête en dict
        data = request.model_dump(by_alias=True)

        # 2. Préparer les données employee
        employee_data = {"user_id": user_id}
        for key, value in data.items():
            employee_data[key.replace(" ", "_")] = value

        # 3. Sauvegarder l’employé
        employee = Employee(**employee_data)
        db.add(employee)
        db.flush()

        # 4. Préparer les features ML
        features = pd.DataFrame([data])
        if hasattr(loaded_model, "feature_names_in_"):
            features = features[loaded_model.feature_names_in_]

        # 5. Prédiction
        prediction = int(loaded_model.predict(features)[0])
        probability = float(loaded_model.predict_proba(features)[0][1])

        # 6. Génération stratégie (SEULEMENT SI RISQUE)
        retention_strategy = None

        if prediction == 1:
            employee_data_for_gemini = {
                "age": request.Age,
                "department": "Non renseigné",
                "job_role": "Non renseigné",
                "job_satisfaction": request.JobSatisfaction,
                "performance": 0,
                "work_life_balance": 0
            }

            gemini_result = generer_plan_retention(
                employee_data_for_gemini,
                churn_probability=round(probability * 100, 2)
            )

            if gemini_result and "retention_plan" in gemini_result:
                retention_strategy = "\n".join(gemini_result["retention_plan"])

        # 7. Sauvegarder l’historique
        history = History(
            user_id=user_id,
            employee_id=employee.id,
            probability=probability,
            retention_strategy=retention_strategy
        )
        db.add(history)

        # 8. Commit
        db.commit()

        # 9. Réponse API
        return {
            "employee_id": employee.id,
            "attrition": prediction,
            "risque": "Élevé" if prediction == 1 else "Faible",
            "retention_strategy": retention_strategy
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()
