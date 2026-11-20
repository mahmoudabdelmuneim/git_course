"""Health endpoint tests."""

def test_health_returns_expected_payload(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "app_name": "AI Home Workout",
        "version": "0.1.0",
    }
