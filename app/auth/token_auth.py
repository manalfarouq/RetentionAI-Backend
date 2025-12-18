from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..core.config import settings

security = HTTPBearer()

# Création du token
def create_token(user_id: int):
    expire = datetime.now(timezone.utc) + timedelta(hours=24)
    payload = {
        "user_id": user_id,
        "exp": expire
    }
    return jwt.encode(payload, settings.SK, algorithm=settings.ALG)


# Vérification du token 
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, settings.SK, algorithms=[settings.ALG])
        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Token invalide")

        return user_id

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expiré")

    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide")
