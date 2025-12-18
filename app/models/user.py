from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from ..db.db_connection import Base 

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    
    # Relation avec AnalyseLog (utiliser string pour éviter l'import circulaire)
    # employee = relationship("Employee", back_populates="user")
