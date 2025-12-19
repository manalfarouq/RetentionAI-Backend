# app/routes/get_all_users_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.token_auth import get_current_user
from app.db.db_connection import get_db
from app.models.employee import Employee
from app.models.history import History

router = APIRouter()


@router.get("/GetAllEmployees")
def get_all_employee(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    result = []
    
    for employee in employees:
        prediction = db.query(History).filter(History.employee_id == employee.id).order_by(History.created_at.desc()).first()
        
        result.append({
            "id": employee.id,
            "name": f"Employee_{employee.id}",
            "prediction": "Va quitter" if prediction and prediction.probability > 0.5 else "Va rester",
            "probability": round(prediction.probability * 100, 2) if prediction else 0,
            "retention_strategy": prediction.retention_strategy if prediction else None
        })

    return {"users": result}