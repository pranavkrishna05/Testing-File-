import pytest
from app.app import create_app

@pytest.fixture
def app():
    return create_app(env='testing')

@pytest.fixture
def client(app):
    return app.test_client()

def test_success_registration(client):
    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "Password123!"
    }
    response = client.post('/api/register', json=payload)
    assert response.status_code == 201
    assert "username" in response.json

def test_existing_email_registration(client):
    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "Password123!"
    }
    client.post('/api/register', json=payload)  # First registration
    response = client.post('/api/register', json=payload)  # Duplicate
    assert response.status_code == 400
    assert "already registered" in response.json["error"]

def test_invalid_email_registration(client):
    payload = {
        "username": "testuser",
        "email": "invalid-email",
        "password": "Password123!"
    }
    response = client.post('/api/register', json=payload)
    assert response.status_code == 400
    assert "Invalid email" in response.json["error"]

