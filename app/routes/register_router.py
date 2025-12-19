# routes/register_router.py
from fastapi import APIRouter, HTTPException
from ..schemas.SignupRequest_schema import SignupRequest
from ..db.db_connection import SessionLocal
from ..models.user import User
from ..auth.token_auth import create_token
import bcrypt

router = APIRouter()

@router.post("/signup", status_code=201)
def register(signup_request: SignupRequest):
    db = SessionLocal()
    try:
        # Vérifie si l'utilisateur existe
        if db.query(User).filter(User.username == signup_request.username).first():
            raise HTTPException(status_code=400, detail="Nom d'utilisateur existant")

        # Hash du mot de passe
        hashed_password = bcrypt.hashpw(
            signup_request.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        # Création utilisateur
        new_user = User(username=signup_request.username, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        token = create_token(new_user.id)

        return {
            "message": "Utilisateur créé",
            "username": new_user.username,
            "token": token
        }
    
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        db.close()