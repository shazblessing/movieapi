from rest_framework import serializers
from .models import Movie
from Review.serializer import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    review = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "author",
            "genre",
            "description",
            "review",
            "rating",
            "release_date",
        ]

    def get_rating(self, obj):
        value = obj.rating.values_list("rating", flat=True)
        average = sum(value) / len(value) if value else 0
        return round(average, 1)
