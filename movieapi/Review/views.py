from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializer import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from Movie.models import Movie


class ReviewDetail(APIView):
    serializer_class = ReviewSerializer
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
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class DeleteReview(APIView):
#     permission_classes = [IsAuthenticated]

#     def delete(self, request, *args, **kwargs):
#         pk = self.kwargs.get("pk")
#         review = get_object_or_404(Review, pk=pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class DeleteReview(APIView):
#     permission_classes = [IsAuthenticated]

    