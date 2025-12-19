-- init.sql
CREATE DATABASE retention_db OWNER retention_user;

\c retention_db

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS employee (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    "Age" INTEGER NOT NULL,
    "JobLevel" INTEGER NOT NULL,
    "MonthlyIncome" INTEGER NOT NULL,
    "StockOptionLevel" INTEGER NOT NULL,
    "TotalWorkingYears" INTEGER,
    "YearsAtCompany" INTEGER,
    "YearsInCurrentRole" INTEGER,
    "YearsWithCurrManager" INTEGER,
    "EnvironmentSatisfaction" INTEGER,
    "JobInvolvement" INTEGER,
    "JobSatisfaction" INTEGER,
    "BusinessTravel_Travel_Frequently" INTEGER,
    "JobRole_Laboratory Technician" INTEGER,
    "JobRole_Research Director" INTEGER,
    "JobRole_Sales Representative" INTEGER,
    "MaritalStatus_Divorced" INTEGER,
    "MaritalStatus_Married" INTEGER,
    "MaritalStatus_Single" INTEGER,
    "OverTime_No" INTEGER,
    "OverTime_Yes" INTEGER
);

CREATE TABLE IF NOT EXISTS history (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    employee_id INTEGER NOT NULL REFERENCES employee(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO retention_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO retention_user;