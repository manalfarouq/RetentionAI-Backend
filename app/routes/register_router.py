from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..schemas.SignupRequest_schema import SignupRequest
from ..db.db_connection import get_db
from ..models.user import User
from ..auth.token_auth import create_jwt_token
import bcrypt

router = APIRouter()


@router.post("/signup", status_code=201)
def register(signup_request: SignupRequest, db: Session = Depends(get_db)):
    try:
        # Vérifier si l'utilisateur existe déjà
        user = db.query(User).filter(User.username == signup_request.username).first()
        if user:
            raise HTTPException(
                status_code=400,
                detail="Ce nom d'utilisateur existe déjà"
            )

        # Hash du mot de passe
        hashed_password = bcrypt.hashpw(
            signup_request.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        # Création utilisateur
        new_user = User(
            username=signup_request.username,
            password=hashed_password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Token JWT
        token = create_jwt_token(new_user.id, new_user.username)

        return {
            "message": "Utilisateur créé avec succès",
            "username": new_user.username,
            "token": token
        }

    except HTTPException:
        raise

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Erreur lors de l'inscription"
        )
