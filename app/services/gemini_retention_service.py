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
    - Age : {employee_data.get('age', 'non renseigné')}
    - Département : {employee_data.get('department', 'non renseigné')}
    - Role : {employee_data.get('job_role', 'non renseigné')}
    - Job Satisfaction : {employee_data.get('job_satisfaction', 'non renseigné')}
    - Performance : {employee_data.get('performance', 'non renseigné')}
    - Work-Life Balance : {employee_data.get('work_life_balance', 'non renseigné')}

    Contexte : ce salarié a un risque élevé de départ ({churn_probability}%).
    Tâche : propose exactement 3 actions concrètes, courtes et opérationnelles pour le retenir.
    Ne fais pas de phrases longues, ni d'explications.
    Répond UNIQUEMENT au format JSON comme ceci :
    {{"retention_plan": ["action1", "action2", "action3"]}}
    Exemple : ["Proposer 2 jours de télétravail", "Réévaluer la charge de déplacement", "Plan de formation personnalisé"]
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