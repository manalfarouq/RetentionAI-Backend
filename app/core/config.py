from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # Variables AUTH
    SK: str
    ALG: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    
    # Variables optionnelles pour autres services
    HF_TOKEN: str 
    GEMINI_API_KEY: str 
    
    class Config:
        env_file = ".env"

settings = Settings()