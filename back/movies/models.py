from django.db import models
from django.conf import settings
# Create your models here.


class Genre(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.CharField(max_length=20)
    overview = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movie', blank=True)
    poster_path = models.TextField()
    release_date = models.DateField()
    backdrop_path = models.TextField(null=True)
    vote_average = models.FloatField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)

class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review, related_name='comments', on_delete=models.CASCADE)
