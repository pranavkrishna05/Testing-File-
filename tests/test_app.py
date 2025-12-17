import pytest
from app.app import app

@pytest.fixture

def client()
    app.config['TESTING'] = True
    with app.test_client() as client
        yield client

def test_get_user(client)
    response = client.get('/users/1')
    assert response.status_code == 404
    assert b'User not found' in response.data
