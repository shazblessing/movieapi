from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rating
from .serializer import RatingSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from Movie.models import Movie


class RatingDetail(APIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        movie = get_object_or_404(Movie, pk=pk)
        serializer = self.serializer_class(data=self.request.data)

        if serializer.is_valid():
            serializer.save(author=self.request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        rating = get_object_or_404(Rating, pk=pk)
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
