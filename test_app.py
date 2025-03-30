import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    return client

def test_get_users(client):
    """Test retrieving users (should return an empty list at first)."""
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json == []

def test_add_user(client):
    """Test adding a new user."""
    response = client.post("/users", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json["name"] == "John Doe"
    assert response.json["email"] == "john@example.com"

def test_update_user(client):
    """Test updating an existing user."""
    client.post("/users", json={"name": "Alice", "email": "alice@example.com"})  # Add user
    response = client.put("/users/1", json={"name": "Alice Updated", "email": "alice@newmail.com"})
    assert response.status_code == 200
    assert response.json["name"] == "Alice Updated"

def test_delete_user(client):
    """Test deleting a user."""
    client.post("/users", json={"name": "Bob", "email": "bob@example.com"})  # Add user
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json["message"] == "User deleted"
