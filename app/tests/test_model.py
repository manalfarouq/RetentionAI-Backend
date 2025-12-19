from app.services import gemini_retention_service

def test_generer_plan_retention(mocker):
    fake_response = {"retention_plan": ["Proposer 2 jours de télétravail", "Plan de formation personnalisé"]}

    mocker.patch(
        "app.services.gemini_retention_service.generer_plan_retention",
        return_value=fake_response
    )

    result = gemini_retention_service.generer_plan_retention("Test prompt")
    assert result == fake_response
