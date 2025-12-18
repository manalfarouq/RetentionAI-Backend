from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from ..db.db_connection import Base 

class History(Base):
    __tablename__ = "history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # user = relationship("User", backref="histories")
    # employee = relationship("Employee", backref="histories")
