import pytest

@pytest.mark.django_db
def test_create_review(api_client, get_tokens):
    tokens = get_tokens("reviewuser", "reviewpass123")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")

    # Create a book first
    book_response = api_client.post(
        "/api/books/",
        {
            "title": "Book for Review",
            "author": "Review Author",
            "published_date": "2025-01-01",
        },
        format="json",
    )
    book_id = book_response.json()["id"]

    # Add a review
    review_response = api_client.post(
        f"/api/books/{book_id}/reviews/add/",
        {"content": "Great book!", "rating": 5},
        format="json",
    )
    assert review_response.status_code == 201
    assert review_response.json()["content"] == "Great book!"
