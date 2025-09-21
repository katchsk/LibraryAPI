import pytest

@pytest.mark.django_db
def test_user_registration(api_client):
    response = api_client.post(
        "/api/users/auth/register/",
        {"username": "newuser", "password": "newpass123"},
        format="json",
    )
    assert response.status_code == 201
    assert "id" in response.json()


@pytest.mark.django_db
def test_jwt_login(api_client, create_user):
    create_user("loginuser", "loginpass123")
    response = api_client.post(
        "/api/users/auth/login/",
        {"username": "loginuser", "password": "loginpass123"},
        format="json",
    )
    assert response.status_code == 200
    assert "access" in response.json()
