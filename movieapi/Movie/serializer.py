from rest_framework import serializers
from .models import Movie
from Review.serializer import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "author",
            "genre",
            "description",
            "review",
            "release_date",
        ]
