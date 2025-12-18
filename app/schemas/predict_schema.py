from pydantic import BaseModel


class PredictRequest(BaseModel):
    """Schéma pour la requête de la prediction"""

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


class PredictResponse(BaseModel):
    """Schéma pour la réponse de la prediction"""

    prediction: int
    probability: float
