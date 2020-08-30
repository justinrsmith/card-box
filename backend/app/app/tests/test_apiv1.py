from fastapi.testclient import TestClient


def test_create_card(client: TestClient):
    response = client.post(
        "/api/v1/cards/", json={"player_name": "Sammy Sosa", "year": 1998}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["player_name"] == "Sammy Sosa"
    assert "id" in data
    card_id = data["id"]

    response = client.get(f"/api/v1/cards/{card_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["player_name"] == "Sammy Sosa"
    assert data["id"] == card_id
