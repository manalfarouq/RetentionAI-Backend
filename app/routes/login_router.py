from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..schemas.LoginRequest_schema import LoginRequest
from ..db.db_connection import get_db
from ..models.user import User
from ..auth.token_auth import create_jwt_token
import bcrypt

router = APIRouter()


@router.post("/login")
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    try:
        # Récupérer l'utilisateur
        user = db.query(User).filter(User.username == login_request.username).first()
        
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Nom d'utilisateur ou mot de passe invalide"
            )
        
        # Vérifier le mot de passe
        if not bcrypt.checkpw(
            login_request.password.encode("utf-8"),
            user.password.encode("utf-8")
        ):
            raise HTTPException(
                status_code=401,
                detail="Nom d'utilisateur ou mot de passe invalide"
            )
        
        # Créer le token
        token = create_jwt_token(user.id, user.username)
        
        return {
            "token": token,
            "user_id": user.id,
            "username": user.username
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erreur lors de la connexion"
        )
