from django.contrib import admin
from .models import Movie, Comment, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Comment)
