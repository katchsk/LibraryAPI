from django.urls import path
from backend.lib.api.books_views import BookListCreateView, BookDetailView
from backend.lib.api.reviews_views import AddReviewView, ListReviewsView
from backend.lib.api.users_views import RegisterView, LoginView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/<int:book_id>/reviews/", ListReviewsView.as_view(), name="list-reviews"),
    path("books/<int:book_id>/reviews/add/", AddReviewView.as_view(), name="add-review"),
    path("users/auth/register/", RegisterView.as_view(), name="register"),
    path("users/auth/login/", LoginView.as_view(), name="login"),
]

