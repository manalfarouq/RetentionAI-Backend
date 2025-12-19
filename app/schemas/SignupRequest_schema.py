from pydantic import BaseModel, Field, EmailStr

class SignupRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Nom d'utilisateur")
    password: str = Field(..., min_length=4, description="Mot de passe")