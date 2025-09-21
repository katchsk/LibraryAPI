import pytest

@pytest.mark.django_db
def test_create_book_authenticated(api_client, get_tokens):
    tokens = get_tokens("bookuser", "bookpass123")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")
    response = api_client.post(
        "/api/books/",
        {"title": "Test Book", "author": "Author Name",
         "published_date": "2025-09-21"},
        format="json",
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"


@pytest.mark.django_db
def test_list_books(api_client, get_tokens):
    tokens = get_tokens("listuser", "listpass123")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")
    response = api_client.get("/api/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
