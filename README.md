# zoroRH - Backend 

**Solution IA pour la Rétention des Talents RH**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat&logo=docker&logoColor=white)
![ML](https://img.shields.io/badge/ML-scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)

---

## Description

**zoroRH** est une application backend intelligente destinée aux équipes **Ressources Humaines** pour **anticiper les départs volontaires** et **proposer automatiquement des plans de rétention personnalisés**.

### Le Système Combine

| Machine Learning |  API Sécurisée |  IA Générative |
|---------------------|------------------|------------------|
| Prédiction risque départ | Auth JWT + PostgreSQL | Plans personnalisés |
| Random Forest optimisé | Traçabilité complète | Google Gemini AI |

---

##  Objectifs

### Business
- ✅ Identifier les profils à **haut risque de démission**
- ✅ Réduire le **turnover** et préserver les talents clés
- ✅ Automatiser l'analyse RH et les recommandations
- ✅ Décisions **objectives et personnalisées**

### Techniques
- ✅ Pipeline **ML supervisé** (Random Forest)
- ✅ API **REST FastAPI** sécurisée
- ✅ Authentification **JWT**
- ✅ Base **PostgreSQL** traçable
- ✅ IA générative **Gemini**
- ✅ **Docker** pour déploiement reproductible

---

##  Fonctionnalités

###  Authentification
- **Inscription** : `POST /register` (hashage bcrypt)
- **Connexion** : `POST /login` (token JWT)
- **Protection** : Middleware JWT sur routes métier

###  Machine Learning
- **Prédiction** : `POST /predict`
  - Probabilité churn 0-100%
  - Niveau risque : LOW/MEDIUM/HIGH
  - Modèle Random Forest optimisé

###  IA Générative
- **Plans rétention** : `POST /generate-retention-plan`
  - Déclenchement si probabilité > 50%
  - Recommandations personnalisées (Gemini AI)
  - Actions concrètes pour managers RH

###  Gestion Données
- **Liste employés** : `GET /employees`
- **Historique prédictions** : Traçabilité PostgreSQL

---

##  Architecture
```
Client RH (Frontend)
        ↓ JWT Token
FastAPI Backend
  ├─ Auth (JWT)
  ├─ Routes API
  ├─ ML Service (modele_attrition_best.pkl)
  └─ IA Service (Gemini)
        ↓
PostgreSQL + Google Gemini AI
```

---

##  Structure du Projet
```
RETENTIONAI-BACKEND/
├── app/
│   ├── auth/
│   │   └── token_auth.py              # JWT logic
│   ├── core/
│   │   └── config.py                  # Variables env
│   ├── db/
│   │   ├── data.csv                   # Dataset ML
│   │   └── db_connection.py           # SQLAlchemy
│   ├── models/                        # ORM Models
│   │   ├── employee.py
│   │   ├── history.py
│   │   └── user.py
│   ├── routes/                        # API Endpoints
│   │   ├── login_router.py
│   │   ├── register_router.py
│   │   ├── prediction_router.py
│   │   ├── retention_router.py
│   │   └── get_all_employees_router.py
│   ├── schemas/                       # Pydantic
│   │   ├── LoginRequest_schema.py
│   │   ├── SignupRequest_schema.py
│   │   ├── PredictRequest_schema.py
│   │   └── retention_schema.py
│   ├── services/                      # Business Logic
│   │   ├── gemini_retention_service.py
│   │   ├── modele_attrition_best.pkl  # ML Model
│   │   ├── pipeline.py
│   │   └── ml_service.ipynb
│   ├── tests/
│   │   └── test_model.py
│   └── main.py                        # Entry point
│
├── .env                               # Secrets (not versioned)
├── .env.example                       # Template
├── docker-compose.yml                 # Docker orchestration
├── Dockerfile                         # Backend image
├── init.sql                           # DB init script
├── requirements.txt                   # Dependencies
└── README.md
```

---

##  Technologies

| Catégorie | Stack |
|-----------|-------|
| **Backend** | FastAPI 0.104+, Uvicorn, Pydantic |
| **ML** | scikit-learn, pandas, numpy, seaborn |
| **IA** | Google Generative AI (Gemini) |
| **Database** | PostgreSQL 15, SQLAlchemy, psycopg2 |
| **Auth** | JWT (python-jose), bcrypt |
| **DevOps** | Docker, Docker Compose, pytest |

---

##  Installation

### Prérequis
- Python 3.11+
- PostgreSQL 15+
- [Clé API Google Gemini](https://makersuite.google.com/app/apikey)
- Docker & Docker Compose (optionnel)

### Installation Locale
```bash
# 1. Cloner le repo
git clone https://github.com/votre-username/zororh-backend.git
cd zororh-backend

# 2. Environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# 3. Dépendances
pip install -r requirements.txt

# 4. Variables d'environnement
cp .env.example .env
# Éditer .env avec vos valeurs
```

### Configuration `.env`
```env
# Google Gemini
GEMINI_API_KEY=your_gemini_api_key

# PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_NAME=retentionai_db
DB_USER=retention_user
DB_PASSWORD=your_password

# JWT
SECRET_KEY=your_secret_key_32_chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Environment
ENVIRONMENT=development
```

**Générer SECRET_KEY :**
```bash
openssl rand -hex 32
```

### Initialiser la Database
```bash
# Créer la DB
psql -U postgres -f init.sql

# Ou manuellement :
psql -U postgres
CREATE DATABASE retentionai_db;
\c retentionai_db
# Copier le contenu de init.sql
```

### Lancer le Serveur
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

 API accessible sur : **http://localhost:8000**  
 Documentation : **http://localhost:8000/docs**

---

##  Installation Docker (Recommandé)
```bash
# Créer .env
cp .env.example .env

# Lancer tout (PostgreSQL + Backend)
docker-compose up -d

# Logs
docker-compose logs -f

# Arrêter
docker-compose down
```

✅ **PostgreSQL** : port 5432  
✅ **FastAPI** : port 8000

---

##  Documentation API

### Base URL
- **Local** : `http://localhost:8000`
- **Docs** : `http://localhost:8000/docs`

---

###  Authentification

#### `POST /register`

**Body :**
```json
{
  "username": "hr_manager",
  "password": "SecurePass123!"
}
```

**Response (201) :**
```json
{
  "message": "Utilisateur créé avec succès",
  "access_token": "eyJhbGci...",
  "token_type": "bearer"
}
```

---

#### `POST /login`

**Body :**
```json
{
  "username": "hr_manager",
  "password": "SecurePass123!"
}
```

**Response (200) :**
```json
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer",
  "username": "hr_manager"
}
```

---

###  Machine Learning (Protégé 🔒)

#### `POST /predict`

**Headers :**
```
Authorization: Bearer your_jwt_token
```

**Body :**
```json
{
  "Age": 35,
  "Department": "Sales",
  "JobRole": "Sales Executive",
  "MonthlyIncome": 5000,
  "YearsAtCompany": 7,
  "JobSatisfaction": 3,
  "WorkLifeBalance": 2,
  "OverTime": "Yes",
  "DistanceFromHome": 15,
  "NumCompaniesWorked": 2
}
```

**Response (200) :**
```json
{
  "employee_id": 12345,
  "churn_probability": 0.78,
  "risk_level": "HIGH",
  "message": "Risque élevé de départ détecté"
}
```

**Niveaux de risque :**
- `0-30%` → LOW
- `30-50%` → MEDIUM
- `50-100%` → HIGH

---

#### `POST /generate-retention-plan`

 Déclenché seulement si **probabilité > 50%**

**Headers :**
```
Authorization: Bearer your_jwt_token
```

**Body :**
```json
{
  "employee_data": {
    "Age": 35,
    "Department": "Sales",
    "JobRole": "Sales Executive",
    "MonthlyIncome": 5000,
    "YearsAtCompany": 7,
    "JobSatisfaction": 3,
    "WorkLifeBalance": 2,
    "OverTime": "Yes",
    "DistanceFromHome": 15
  },
  "churn_probability": 0.78
}
```

**Response (200) :**
```json
{
  "retention_plan": "1. Proposer 2 jours télétravail\n2. Réévaluer déplacements\n3. Formation personnalisée\n4. Entretien individuel prioritaire",
  "risk_level": "HIGH",
  "generated_at": "2025-12-19T14:30:00Z"
}
```

---

###  Gestion Données

#### `GET /employees`

**Headers :**
```
Authorization: Bearer your_jwt_token
```

**Query Params (optionnel) :**
- `department` : Filtrer par département
- `limit` : Nombre max résultats (défaut: 100)

**Response (200) :**
```json
{
  "employees": [
    {
      "id": 1,
      "age": 35,
      "department": "Sales",
      "job_role": "Sales Executive",
      "monthly_income": 5000
    }
  ],
  "total": 1
}
```

---

##  Machine Learning Pipeline

### 1. Analyse Exploratoire (EDA)
```python
import pandas as pd
import seaborn as sns

df = pd.read_csv('app/db/data.csv')

# Corrélations
sns.heatmap(df.corr(), annot=True)

# Distribution
sns.countplot(data=df, x='Attrition')
```

**Insights :**
- Variables clés : `OverTime`, `JobSatisfaction`, `WorkLifeBalance`
- Déséquilibre : ~16% attrition

---

### 2. Preprocessing
```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Features
numeric = ['Age', 'MonthlyIncome', 'YearsAtCompany']
categorical = ['Department', 'JobRole', 'OverTime']

# Pipeline
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric),
    ('cat', OneHotEncoder(drop='first'), categorical)
])
```

---

### 3. Entraînement
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# GridSearch
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None]
}

grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid.fit(X_train, y_train)
best_model = grid.best_estimator_
```


---

### 4. Sauvegarde
```python
import pickle

with open('modele_attrition_best.pkl', 'wb') as f:
    pickle.dump(best_model, f)
```

---

##  IA Générative - Gemini

### Prompt Template
```python
prompt = f"""
Tu es un expert RH. Voici les infos employé :

- Âge : {age}
- Département : {department}
- Rôle : {job_role}
- Satisfaction : {job_satisfaction}/4
- Work-Life Balance : {work_life_balance}/4
- Heures sup : {overtime}
- Distance : {distance_from_home} km

Risque départ ML : {churn_probability*100:.1f}%

Propose 3-4 actions concrètes pour le retenir.
Format : opérationnel pour manager RH.
"""
```

### Exemple Réponse
```
1. Proposer 2 jours télétravail/semaine
2. Réévaluer charge déplacements (15km)
3. Formation certifiante management
4. Entretien individuel sous 7 jours
```

---

##  Base de Données

### Schéma
```sql
-- Users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Employees
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    age INTEGER,
    department VARCHAR(100),
    job_role VARCHAR(100),
    monthly_income INTEGER,
    years_at_company INTEGER,
    job_satisfaction INTEGER CHECK (job_satisfaction BETWEEN 1 AND 4),
    work_life_balance INTEGER CHECK (work_life_balance BETWEEN 1 AND 4),
    overtime VARCHAR(10),
    distance_from_home INTEGER
);

-- Predictions History
CREATE TABLE predictions_history (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT NOW(),
    user_id INTEGER REFERENCES users(id),
    employee_id INTEGER,
    probability FLOAT CHECK (probability BETWEEN 0 AND 1),
    risk_level VARCHAR(20),
    retention_plan TEXT
);
```

---

##  Tests
```bash
# Tous les tests
pytest app/tests/ -v

# Avec couverture
pytest app/tests/ --cov=app

# Tests spécifiques
pytest app/tests/test_model.py -v
```

### Exemple Test
```python
def test_model_loading():
    with open('app/services/modele_attrition_best.pkl', 'rb') as f:
        model = pickle.load(f)
    assert model is not None

def test_prediction():
    sample = {"Age": 35, "Department": "Sales", "MonthlyIncome": 5000}
    prediction = model.predict_proba([sample])[0][1]
    assert 0 <= prediction <= 1
```

---

## Exemples Utilisation

### cURL
```bash
# Inscription
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"test123"}'

# Connexion
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"test123"}'

# Prédiction
TOKEN="your_jwt_token"
curl -X POST http://localhost:8000/predict \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "Age": 35,
    "Department": "Sales",
    "JobRole": "Sales Executive",
    "MonthlyIncome": 5000,
    "YearsAtCompany": 7,
    "JobSatisfaction": 3,
    "WorkLifeBalance": 2,
    "OverTime": "Yes",
    "DistanceFromHome": 15,
    "NumCompaniesWorked": 2
  }'
```

---

### Python
```python
import requests

BASE_URL = "http://localhost:8001"

# Login
r = requests.post(f"{BASE_URL}/login", json={
    "username": "test", "password": "test123"
})
token = r.json()["access_token"]

# Predict
headers = {"Authorization": f"Bearer {token}"}
data = {
    "Age": 35, "Department": "Sales",
    "JobRole": "Sales Executive",
    "MonthlyIncome": 5000,
    "YearsAtCompany": 7,
    "JobSatisfaction": 3,
    "WorkLifeBalance": 2,
    "OverTime": "Yes",
    "DistanceFromHome": 15,
    "NumCompaniesWorked": 2
}

result = requests.post(f"{BASE_URL}/predict", json=data, headers=headers)
print(f"Risque : {result.json()['churn_probability']*100:.1f}%")
```

---

##  Sécurité

- **JWT** : Tokens expirables (24h)
- **Bcrypt** : Hashage mots de passe
- **CORS** : Configurer origines autorisées en production
- **SQL Injection** : Protection via ORM SQLAlchemy
- **Validation** : Pydantic sur toutes les entrées

---

##  Liens Utiles

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [Gemini AI Docs](https://ai.google.dev/docs)
- [scikit-learn Guide](https://scikit-learn.org/stable/user_guide.html)
