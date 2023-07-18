from ..models import Movie, Review, Comment
from rest_framework import serializers
from .user import UserSerializer
from django.contrib.auth import get_user_model
from django.db.models import Count
    # class CommentSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Comment
    #         fields = '__all__'
    # comments = CommentSerializer(many=True)

class ReviewListSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title','id')
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
    comments = CommentSerializer(many=True, read_only=True)
    
    comment_count = serializers.IntegerField(source='comments.count',read_only=True)

    class Meta:
        model = Review
        fields= '__all__'
    #comments 갯수를 출력할 comments_count class 정의
    # def get_count_comments(self,obj):
    #     return obj.Comment.Count()

class ReviewSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)
        class Meta:
            model = Comment
            fields = ('content','user','id')
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title','id')
    movie = MovieSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

