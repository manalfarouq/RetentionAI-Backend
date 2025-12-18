# routes/prediction.py
from fastapi import APIRouter, HTTPException, Depends
from ..schemas.PredictRequest_schema import PredictRequest
from ..db.db_connection import SessionLocal
from ..models.employee import Employee
from ..models.history import History
from ..auth.token_auth import get_current_user
import joblib
import pandas as pd

router = APIRouter()

# Charger le modèle ML une seule fois au démarrage
loaded_model = joblib.load("app/services/modele_attrition_best.pkl")

@router.post("/predict")
def predict(request: PredictRequest, user_id: int = Depends(get_current_user)):
    """
    Fonction de prédiction d'attrition d'un employé
    - Reçoit les données d'un employé
    - Sauvegarde dans la base de données
    - Fait une prédiction avec le modèle ML
    - Retourne le résultat
    """
    
    # 1. Ouvrir connexion base de données
    db = SessionLocal()
    
    try:
        # 2. Convertir les données reçues en dictionnaire
        data = request.model_dump(by_alias=True)
        
        # 3. Remplacer les espaces par des underscores dans les noms
        # Exemple: "JobRole_Laboratory Technician" → "JobRole_Laboratory_Technician"
        employee_data = {}
        employee_data["user_id"] = user_id
        for key, value in data.items():
            new_key = key.replace(" ", "_")
            employee_data[new_key] = value

        # 4. Sauvegarder l'employé dans la base de données
        employee = Employee(**employee_data)
        db.add(employee)
        db.flush()  # Récupère l'ID sans finaliser la transaction

        # 5. Préparer les données pour la prédiction
        features = pd.DataFrame([data])
        if hasattr(loaded_model, "feature_names_in_"):
            features = features[loaded_model.feature_names_in_]
        
        # 6. Faire la prédiction (0 = pas de risque, 1 = risque)
        prediction = int(loaded_model.predict(features)[0])

        # 7. Sauvegarder l'historique
        history = History(user_id=user_id, employee_id=employee.id)
        db.add(history)
        
        # 8. Valider toutes les modifications
        db.commit()

        # 9. Retourner le résultat
        return {
            "employee_id": employee.id,
            "attrition": prediction,
            "risque": "Élevé" if prediction == 1 else "Faible"
        }
    
    except Exception as e:
        # En cas d'erreur, annuler les modifications
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # Toujours fermer la connexion
        db.close()