# app/schemas/retention_schema.py
from pydantic import BaseModel, Field

class RetentionPlanRequest(BaseModel):
    age: int
    department: str
    job_role: str
    job_satisfaction: int
    performance: int
    work_life_balance: int
    churn_probability: float = Field(..., ge=0, le=100)

class RetentionPlanResponse(BaseModel):
    retention_plan: list[str]
