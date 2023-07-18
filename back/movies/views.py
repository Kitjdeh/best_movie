from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Comment, Review, Genre
from .serializers.comment import CommentSerializer
from .serializers.review import ReviewListSerializer, ReviewSerializer
from .serializers.movie import MovieListSerializer, MovieSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
import requests
from django.http import HttpResponse, JsonResponse
from django.db import models

API_KEY = 'a8fa836c288fad1019bf59decf6c54eb'
GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'


# Create your views here.
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def likemovies(request):
    # 좋아요숫자로 카운팅하여 상위 5개만 컷
    movies = Movie.objects.annotate(like_count=Count(
        'like_users')).order_by('-like_count')[:5]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def toprated(request):
    movies = Movie.objects.order_by('-vote_average')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movieslist(request):
    movies = get_list_or_404(Movie)
    # movies = movies[0:5]
    # movies[0].get('genres') = {'change'}
    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def moviedetail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def wishlist(request):
    user = request.user
    movies = Movie.objects.filter(like_users__in=[user.pk])
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def reviews(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        movie = get_object_or_404(Movie, pk=request.data['movie'])
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def reviewdetail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie = get_object_or_404(Movie, pk=request.data['movie'])
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            # serializer.save()
            # serializer = ReviewSerializer(review)

        return Response(serializer.data, status.HTTP_202_ACCEPTED)
    else:
        serializer = ReviewSerializer(review)
    return Response(serializer.data)


#유저가 좋아요를 누른 movie 추출
@api_view(['POST'])
def movielike(request, movie_pk):
    # movies = Movie.objects.annotate(like_count=Count(
    #     'like_users')).order_by('-like_count')[:5]
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.id).exists():
        movie.like_users.remove(user)
        # movie.objects.annotate(like=)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def search(request, movietitle):
    movie = Movie.objects.filter(title__icontains=movietitle)
    serializer = MovieListSerializer(movie, many=True)
    return Response(serializer.data)


# def populat_movie_data(page=1):
#     response = requests.get(
#         POPULAR_MOVIE_URL,
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',
#             'page': page,
#         }
#     ).json()
#     for genre in response.get('genres'):
#         Genre.objects.create(
#             id=genre.get('id'),
#             name=genre.get('name')
#         )
#     return JsonResponse(response)

# 1.해당 user가 좋아요 누른 영화 id목록 movie출력
# 1-1. movie_list의 각 영화들의 장르 id 값들 누적 append 한 genre_list생성
# 2. dict 배열 생성
# 3-1.movie_list for문
# 3-2.각 영화의 genre값 for문
# 4-1. 해당 genre (key값)당 value 값 +1
# 4-2. 해당 genre 값이 없으면 1로 생성
# 5. 가장 높은 value 값의 target_genre 선출

@api_view(['GET'])
def preference_genre(request):
    user = request.user
    movie_list = []
    genre_list = []
    # 1.해당 user가 좋아요 누른 영화 id목록 movie출력
    movies = Movie.objects.filter(like_users__exact=user.id)
    # 2. dict 배열 생성
    count_genres = {}
    # 3-1.movie for문
    for movie in movies:
        genres = movie.genres.all()

        # 3-2.각 영화의 genre값 for문
        for genre in genres.values():
            # 4-1. 해당 genre (key값)당 value 값 +1
            if count_genres.get(f"{genre['id']}"):
                count_genres[f"{genre['id']}"] += 1
            # 4-2. 해당 genre 값이 없으면 1로 생성
            else:
                count_genres[f"{genre['id']}"] = 1
    # 5. 가장 높은 value 값의 target_genre 선출
    max_genres_id = max(count_genres, key=count_genres.get)
    movies = Movie.objects.filter(
        genres__in=[max_genres_id]).order_by('-vote_average')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def reviewcomment(request, review_pk):
    if request.method == 'GET':
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    if request.method == 'POST':
        review = get_object_or_404(Review, pk=review_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def updatecomment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            # serializer.save()
            # serializer = ReviewSerializer(review)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
    else:
        serializer = ReviewSerializer(review)
    return Response(serializer.data)
