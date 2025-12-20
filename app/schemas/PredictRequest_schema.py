from pydantic import BaseModel, Field
from typing import Literal

class PredictRequest(BaseModel):
    Age: int
    JobLevel: int
    MonthlyIncome: float
    StockOptionLevel: int
    TotalWorkingYears: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsWithCurrManager: int

    EnvironmentSatisfaction: int
    JobInvolvement: int
    JobSatisfaction: int

    BusinessTravel_Travel_Frequently: int

    JobRole_Laboratory_Technician: int
    JobRole_Research_Director: int
    JobRole_Sales_Representative: int

    MaritalStatus_Divorced: int
    MaritalStatus_Married: int
    MaritalStatus_Single: int
    OverTime_No: int
    OverTime_Yes: int



