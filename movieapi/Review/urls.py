from django.urls import path
from .views import ReviewDetail


urlpatterns = [
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review_detail"),
]
