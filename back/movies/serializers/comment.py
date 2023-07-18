from ..models import Movie, Review, Comment
from rest_framework import serializers
from .user import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title')
    review = ReviewSerializer
    class Meta:
        model = Comment
        fields = '__all__'

