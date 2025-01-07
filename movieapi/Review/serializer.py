from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ["id", "movie", "review", "author"]
        read_only_fields = ["author", "movie"]
