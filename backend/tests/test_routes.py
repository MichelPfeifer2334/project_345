from backend.app import models

def test_create_question(client, db):
    # Test-Daten für die Frage und die Wahlmöglichkeiten
    question_data = {
        "question_text": "Was ist die Hauptstadt von Deutschland?",
        "choices": [
            {"choice_text": "Berlin", "is_correct": True},
            {"choice_text": "Hamburg", "is_correct": False},
            {"choice_text": "München", "is_correct": False}
        ]
    }
    # Sende POST-Anfrage an den Endpunkt
    response = client.post("/questions/", json=question_data)
    
    # Überprüfen ob die Antwort korrekt ist
    assert response.status_code == 200
    data = response.json()
    assert "question_id" in data
    assert data["message"] == "Question created successfully"

    # Frage aus der Datenbank holen
    question_id = data["question_id"]
    db_question = db.query(models.Question).filter(models.Question.id == question_id).first()
    assert db_question is not None
    assert db_question.question_text == "Was ist die Hauptstadt von Deutschland?"

    # Choices überprüfen
    choices = db.query(models.Choices).filter(models.Choices.question_id == question_id).all()
    assert len(choices) == 3
    assert choices[0].choice_text == "Berlin"
    # assert choices[0].choice_text == "Hamburg"
    # assert choices[0].choice_text == "München"

