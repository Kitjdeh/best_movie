from ..models import Movie, Review, Comment, Genre
from rest_framework import serializers
from .user import UserSerializer
from django.db.models import Count
from accounts.models import User

class MovieListSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    genres = GenreSerializer(many=True, read_only=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'id')
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'

        class CommentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Comment
                fields = ('content', 'user', 'id')
        comments = CommentSerializer(many=True, read_only=True)
    
    review_set = ReviewSerializer(many=True, read_only=True)

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    genres = GenreSerializer(many=True, read_only=True)
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username','id')
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'