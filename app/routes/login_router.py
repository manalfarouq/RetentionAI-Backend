# routes/login.py
from fastapi import APIRouter, HTTPException
from ..schemas.LoginRequest_schema import LoginRequest
from ..db.db_connection import SessionLocal
from ..models.user import User
from ..auth.token_auth import create_token
import bcrypt

router = APIRouter()

@router.post("/login")
def login(login_request: LoginRequest):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == login_request.username).first()
        
        if not user:
            raise HTTPException(status_code=401, detail="Identifiants invalides")
        
        # Vérifie le mot de passe
        if not bcrypt.checkpw(login_request.password.encode("utf-8"), user.password.encode("utf-8")):
            raise HTTPException(status_code=401, detail="Identifiants invalides")
        
        token = create_token(user.id)
        
        return {
            "token": token,
            "user_id": user.id,
            "username": user.username
        }
    
    finally:
        db.close()