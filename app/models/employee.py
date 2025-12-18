from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from ..db.db_connection import Base



class Employee(Base):
    __tablename__ = "employee"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    Age = Column(Integer, nullable=False)
    JobLevel = Column(Integer, nullable=False)
    MonthlyIncome = Column(Integer, nullable=False)
    StockOptionLevel = Column(Integer, nullable=False)
    TotalWorkingYears = Column(Integer)
    YearsAtCompany = Column(Integer)
    YearsInCurrentRole = Column(Integer)
    YearsWithCurrManager = Column(Integer)

 
    EnvironmentSatisfaction = Column(Integer)
    JobInvolvement = Column(Integer)
    JobSatisfaction = Column(Integer)

    BusinessTravel_Travel_Frequently = Column(Integer)
    JobRole_Laboratory_Technician = Column("JobRole_Laboratory Technician", Integer)
    JobRole_Research_Director = Column("JobRole_Research Director", Integer)
    JobRole_Sales_Representative = Column("JobRole_Sales Representative", Integer)
    MaritalStatus_Divorced = Column(Integer)
    MaritalStatus_Married = Column(Integer)
    MaritalStatus_Single = Column(Integer)
    OverTime_No = Column(Integer)
    OverTime_Yes = Column(Integer)

    
    
    # user = relationship("User", back_populates="employee")