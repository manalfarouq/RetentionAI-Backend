# app/services/gemini_retention_service.py
import google.generativeai as genai
from app.core.config import settings
import json

genai.configure(api_key=settings.GEMINI_API_KEY)

def generer_plan_retention(employee_data: dict, churn_probability: float):
    """
    Génère un plan de rétention RH via Gemini
    """
    prompt = f"""
Agis comme un expert RH.
Voici les informations sur l'employé :
- Age : {employee_data['age']}
- Département : {employee_data['department']}
- Role : {employee_data['job_role']}
- Job Satisfaction : {employee_data['job_satisfaction']}
- Performance : {employee_data['performance']}
- Work-Life Balance : {employee_data['work_life_balance']}

Contexte : ce salarié a un risque élevé de départ ({churn_probability}%).
Tache : propose 3 actions concrètes pour le retenir.
Répond UNIQUEMENT au format JSON : {{"retention_plan": ["action1","action2","action3"]}}
"""

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        texte = response.text.strip()

        # Nettoyage
        if "```json" in texte:
            texte = texte.replace("```json", "").replace("```", "")

        return json.loads(texte)

    except Exception as e:
        return {"retention_plan": None, "erreur": str(e)}