from django.db import models
from django.contrib.auth.models import User
from Movie.models import Movie

# Create your models here.


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
    review = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title
