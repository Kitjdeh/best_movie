from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('movies/', views.movieslist, name='movieslist'),
    path('movies/<int:movie_pk>/', views.moviedetail, name='moviedetail'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('reviews/', views.reviews, name='reviews'),
    path('reviews/<int:review_pk>/', views.reviewdetail, name='reviewdetail'),
    # path('reviews/create/', views.reviewcreate, name='reviewcreate'),
    path('movies/<int:movie_pk>/like/', views.movielike, name='movielike'),
    # 좋아요 많은받은 상위 5개 영화 리스트
    path('likemovies/', views.likemovies, name='likemovies'),
    path('toprated/', views.toprated, name='toprated'),
    # 영화 검색기능
    path('search/<str:movietitle>/', views.search, name='search'),
    # 유저의 좋아요 영화리스트에서 가장 많이 중복된 장르의 영화 출력
    path('genre/', views.preference_genre, name='search'),
    # 댓글 생성기능
    path('reviews/<int:review_pk>/comment/',
         views.reviewcomment, name='reviewcomment'),
    # 댓글 수정기능
    path('reviews/<int:review_pk>/comment/<int:comment_pk>/',
         views.updatecomment, name='updatecomment'),


]
