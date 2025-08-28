import pytest
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_show_summary_valid_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Welcome, john@simplylift.co' in response.data
    assert b'Points available' in response.data

def test_show_summary_invalid_email(client):
    response = client.post('/showSummary', data={'email': 'fake@club.co'}, follow_redirects=True)
    assert response.status_code == 200
    # Vérifie que l’on revient bien sur la page index
    assert b'<form' in response.data

