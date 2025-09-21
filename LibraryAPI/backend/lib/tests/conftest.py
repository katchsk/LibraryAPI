import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user():
    def make_user(username="testuser", password="testpass123"):
        return User.objects.create_user(username=username, password=password)
    return make_user


@pytest.fixture
def get_tokens(api_client, create_user):
    def login(username="testuser", password="testpass123"):
        user = create_user(username=username, password=password)
        response = api_client.post(
            "/api/users/auth/login/",
            {"username": username, "password": password},
            format="json",
        )
        assert response.status_code == 200
        return response.json()
    return login
