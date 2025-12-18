from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from ..db.db_connection import Base 

class History(Base):
    __tablename__ = "history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    probability = Column(Float, nullable=False)
    
    # user = relationship("User", backref="histories")
    # employee = relationship("Employee", backref="histories")
