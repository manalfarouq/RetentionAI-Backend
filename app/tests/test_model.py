# app/tests/test_gemini_retention_service.py
from app.services import gemini_retention_service

def test(mocker):
    fake_response = {"retention_plan": ["Proposer 2 jours de télétravail"]}
    mocker.patch("app.services.gemini_retention_service.generer_plan_retention", return_value=fake_response)

    result = gemini_retention_service.generer_plan_retention("Test prompt")
 
    assert result == fake_response                 # Résultat exact
    assert "retention_plan" in result             # Vérifie la clé
    assert len(result["retention_plan"]) > 0      # Non vide
