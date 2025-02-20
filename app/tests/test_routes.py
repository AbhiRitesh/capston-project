import pytest
from app import create_app, db
from app.models import User
from app.auth import auth

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_add_user(client):
    # Add authentication credentials
    auth = ('admin', 'admin123')  # Replace with your username and password
    response = client.post(
        '/users',
        json={'username': 'test', 'email': 'test@example.com'},
        headers={'Authorization': 'Basic ' + auth}
    )
    assert response.status_code == 201

def test_get_users(client):
    # Add authentication credentials
    auth = ('admin', 'admin123')  # Replace with your username and password
    client.post(
        '/users',
        json={'username': 'test', 'email': 'test@example.com'},
        headers={'Authorization': 'Basic ' + auth}
    )
    response = client.get('/users', headers={'Authorization': 'Basic ' + auth})
    assert response.status_code == 200