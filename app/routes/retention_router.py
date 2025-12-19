# app/routers/retention_router.py
from fastapi import APIRouter, Header, HTTPException
from app.schemas.retention_schema import RetentionPlanRequest, RetentionPlanResponse
from app.services.gemini_retention_service import generer_plan_retention
from app.auth.token_auth import get_current_user
from app.db.db_connection import SessionLocal
from app.models.history import History

router = APIRouter(prefix="/generate-retention-plan", tags=["Retention"])

@router.post("", response_model=RetentionPlanResponse)
def generate_retention_plan(data: RetentionPlanRequest, token: str = Header(None)):
    # Vérifier token
    if not token:
        raise HTTPException(status_code=401, detail="Token manquant")
    
    user_id = get_current_user(token.replace("Bearer ", ""))

    # Vérifier probabilité
    if data.churn_probability < 50:
        raise HTTPException(
            status_code=400,
            detail="Churn inférieur à 50%, aucun plan requis"
        )

    # Préparer données
    employee_data = {
        "age": data.age,
        "department": data.department,
        "job_role": data.job_role,
        "job_satisfaction": data.job_satisfaction,
        "performance": data.performance,
        "work_life_balance": data.work_life_balance
    }

    # Générer plan
    resultat = generer_plan_retention(employee_data, data.churn_probability)

    if "erreur" in resultat:
        raise HTTPException(status_code=500, detail=resultat["erreur"])

    # Sauvegarder
    db = SessionLocal()
    try:
        prediction = History(
            user_id=user_id,
            employee_id=data.employee_id,
            probability=float(data.churn_probability),
            retention_strategy="\n".join(resultat["retention_plan"])
        )
        db.add(prediction)
        db.commit()
        db.refresh(prediction)
    except Exception as e:
        db.rollback()
        print(f"Erreur DB: {str(e)}")  # Pour déboguer
        raise HTTPException(status_code=500, detail=f"Erreur lors de la sauvegarde: {str(e)}")
    finally:
        db.close()

    return {"retention_plan": resultat["retention_plan"]}