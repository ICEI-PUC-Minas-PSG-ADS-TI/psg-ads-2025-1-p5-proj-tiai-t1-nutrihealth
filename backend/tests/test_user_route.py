from tests.conftest import client, auth_headers, init_database
from src.models.user_model import User
import pytest

def test_register_user_success(client, init_database):
    data = {"name": "John Doe", "email": "john@example.com", "password": "password123", "tipo": "Cliente"}
    response = client.post("/auth/register", json=data)
    assert response.status_code == 201
    assert "message" in response.json
    assert "id" in response.json
    with client.application.app_context():
        user = User.query.filter_by(email="john@example.com").first()
        assert user is not None
        assert user.name == "John Doe"
        assert user.tipo == "Cliente"

def test_register_user_missing_data(client, init_database):
    data = {"name": "John Doe", "email": "john@example.com"}
    response = client.post("/auth/register", json=data)
    assert response.status_code == 400
    assert "error" in response.json

def test_register_user_email_exists(client, init_database):
    data = {"name": "Jane Doe", "email": "jane@example.com", "password": "password123", "tipo": "Cliente"}
    client.post("/auth/register", json=data)
    response = client.post("/auth/register", json=data)
    assert response.status_code == 409
    assert "error" in response.json

def test_login_user_success(client, init_database):
    register_data = {"name": "Test User", "email": "test@example.com", "password": "password123", "tipo": "Cliente"}
    client.post("/auth/register", json=register_data)
    login_data = {"email": "test@example.com", "password": "password123"}
    response = client.post("/auth/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json

def test_login_user_invalid_credentials(client, init_database):
    register_data = {"name": "Test User", "email": "test@example.com", "password": "password123", "tipo": "Cliente"}
    client.post("/auth/register", json=register_data)
    login_data = {"email": "test@example.com", "password": "wrongpassword"}
    response = client.post("/auth/login", json=login_data)
    assert response.status_code == 401
    assert "error" in response.json

def test_get_user_profile_success(client, auth_headers):
    response = client.get("/profile", headers=auth_headers)
    assert response.status_code == 200
    assert "name" in response.json
    assert response.json["name"] == "Test User"

def test_get_user_profile_invalid_token(client, init_database):
    headers = {"Authorization": "Bearer invalid_token"}
    response = client.get("/profile", headers=headers)
    assert response.status_code == 422 
    
def test_get_user_created_recipes(client, auth_headers, create_test_recipe):
    recipe_id, recipe_data = create_test_recipe
    response = client.get("/profile/my_recipes", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["id"] == recipe_id
    assert response.json[0]["nome"] == recipe_data["nome"]

def test_update_user_success(client, auth_headers, init_database):
    with client.application.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        user_id = user.id
    update_data = {"name": "Updated Name", "email": "updated@example.com"}
    response = client.put(f"/users/{user_id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    assert "message" in response.json
    with client.application.app_context():
        updated_user = User.query.get(user_id)
        assert updated_user.name == "Updated Name"
        assert updated_user.email == "updated@example.com"

def test_update_user_unauthorized(client, init_database):
    client.post("/auth/register", json={"name": "User 1", "email": "user1@example.com", "password": "password1", "tipo": "Cliente"})
    client.post("/auth/register", json={"name": "User 2", "email": "user2@example.com", "password": "password2", "tipo": "Cliente"})
    login_response = client.post("/auth/login", json={"email": "user1@example.com", "password": "password1"})
    user1_token = login_response.json["access_token"]
    user1_headers = {"Authorization": f"Bearer {user1_token}"}
    with client.application.app_context():
        user2 = User.query.filter_by(email="user2@example.com").first()
        user2_id = user2.id
    update_data = {"name": "Updated User 2"}
    response = client.put(f"/users/{user2_id}", json=update_data, headers=user1_headers)
    assert response.status_code == 403

def test_delete_user(client, init_database):
    register_data = {"name": "User to Delete", "email": "delete@example.com", "password": "password123", "tipo": "Cliente"}
    client.post("/auth/register", json=register_data)
    with client.application.app_context():
        user_to_delete = User.query.filter_by(email="delete@example.com").first()
        user_id = user_to_delete.id
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert "message" in response.json
    with client.application.app_context():
        deleted_user = User.query.get(user_id)
        assert deleted_user is None