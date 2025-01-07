from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import MovieSerializer
from .models import Movie
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# The `MovieList` class is an API view in Python that retrieves a list of movies from the database.
class CreateMovie(APIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # user = self.kwargs.get("pk")
        # if user != self.request.user.id:
        #     return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.serializer_class(data=self.request.data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieList(APIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = self.serializer_class(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
