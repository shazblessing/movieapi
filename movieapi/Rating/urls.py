from django.urls import path
from .views import RatingDetail

urlpatterns = [
    path("rating/<int:pk>/", RatingDetail.as_view(), name="rating_detail"),
]
