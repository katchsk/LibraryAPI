from rest_framework import serializers
from backend.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Review
        fields = ["id", "username", "book", "rating", "content"] 
