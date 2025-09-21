from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews"
    )
    book = models.ForeignKey(
        "backend.Book", on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.rating})"

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
