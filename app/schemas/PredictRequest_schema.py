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

    # Ordinales avec valeurs autorisées
    EnvironmentSatisfaction: Literal[1, 2, 3, 4]
    JobInvolvement: Literal[1, 2, 3, 4]
    JobSatisfaction: Literal[1, 2, 3, 4]

    BusinessTravel_Travel_Frequently: int
    JobRole_Laboratory_Technician: int = Field(..., alias="JobRole_Laboratory Technician")
    JobRole_Research_Director: int = Field(..., alias="JobRole_Research Director")
    JobRole_Sales_Representative: int = Field(..., alias="JobRole_Sales Representative")
    MaritalStatus_Divorced: int
    MaritalStatus_Married: int
    MaritalStatus_Single: int
    OverTime_No: int
    OverTime_Yes: int

