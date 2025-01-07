from django.urls import path
from .views import MovieList, CreateMovie

urlpatterns = [
    path("movies/", MovieList.as_view(), name="movies"),
    path("movie/", CreateMovie.as_view(), name="create_movie"),
]
