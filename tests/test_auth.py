from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register_user():
    """Test user registration."""
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword123",
        "full_name": "Test User"
    }

    response = client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == 200

    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["username"] == user_data["username"]
    assert "id" in data
    assert "hashed_password" not in data


def test_register_duplicate_email():
    """Test registration with duplicate email."""
    user_data = {
        "email": "duplicate@example.com",
        "username": "user1",
        "password": "password123"
    }

    # First registration
    response = client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == 200

    # Second registration with same email
    user_data["username"] = "user2"
    response = client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]


def test_register_duplicate_username():
    """Test registration with duplicate username."""
    user_data = {
        "email": "user1@example.com",
        "username": "duplicateuser",
        "password": "password123"
    }

    # First registration
    response = client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == 200

    # Second registration with same username
    user_data["email"] = "user2@example.com"
    response = client.post("/api/v1/auth/register", json=user_data)
    assert response.status_code == 400
    assert "Username already taken" in response.json()["detail"]


def test_login_user():
    """Test user login."""
    # First register a user
    user_data = {
        "email": "login@example.com",
        "username": "loginuser",
        "password": "loginpassword123"
    }

    register_response = client.post("/api/v1/auth/register", json=user_data)
    assert register_response.status_code == 200

    # Then login
    login_data = {
        "username": user_data["username"],
        "password": user_data["password"]
    }

    response = client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == 200

    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials():
    """Test login with invalid credentials."""
    login_data = {
        "username": "nonexistent",
        "password": "wrongpassword"
    }

    response = client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]


def test_get_current_user():
    """Test getting current user information."""
    # Register and login
    user_data = {
        "email": "current@example.com",
        "username": "currentuser",
        "password": "currentpassword123"
    }

    register_response = client.post("/api/v1/auth/register", json=user_data)
    assert register_response.status_code == 200

    login_data = {
        "username": user_data["username"],
        "password": user_data["password"]
    }

    login_response = client.post("/api/v1/auth/login", data=login_data)
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    # Get current user
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/v1/auth/me", headers=headers)
    assert response.status_code == 200

    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["username"] == user_data["username"]


def test_get_current_user_invalid_token():
    """Test getting current user with invalid token."""
    headers = {"Authorization": "Bearer invalid_token"}
    response = client.get("/api/v1/auth/me", headers=headers)
    assert response.status_code == 401
