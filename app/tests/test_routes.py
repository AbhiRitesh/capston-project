import pytest
from app import app, db
from app.models import User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_add_user(client):
    response = client.post('/users', json={'username': 'test', 'email': 'test@example.com'})
    assert response.status_code == 201

def test_get_users(client):
    client.post('/users', json={'username': 'test', 'email': 'test@example.com'})
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json) == 1