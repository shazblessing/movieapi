from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateTimeField()

    def __str__(self):
        return self.title
