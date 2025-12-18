# routes/prediction.py
from fastapi import APIRouter, HTTPException, Depends
from ..schemas.PredictRequest_schema import PredictRequest
from ..db.db_connection import SessionLocal
from ..models.employee import Employee
from ..models.history import History
import joblib
import pandas as pd
from ..auth.token_auth import get_current_user

router = APIRouter()
loaded_model = joblib.load("app/services/modele_attrition_best.pkl")

@router.post("/predict")
def predict(
    request: PredictRequest,
    user_id: int = Depends(get_current_user)
):
    db = SessionLocal()
    try:
        data = request.model_dump(by_alias=True)
        
        # Mapping des clés avec espaces
        employee_data = {
            "user_id": user_id,
            **{k.replace(" ", "_"): v for k, v in data.items()}
        }

        # Sauvegarde
        employee = Employee(**employee_data)
        db.add(employee)
        db.flush()

        # Prédiction
        features = pd.DataFrame([data])
        if hasattr(loaded_model, "feature_names_in_"):
            features = features[loaded_model.feature_names_in_]
        
        prediction = int(loaded_model.predict(features)[0])

        # Historique
        history = History(user_id=user_id, employee_id=employee.id)
        db.add(history)
        db.commit()

        return {
            "employee_id": employee.id,
            "attrition": prediction,
            "risque": "Élevé" if prediction == 1 else "Faible"
        }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        db.close()