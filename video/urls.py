from django.urls import path
from .views import VideoView


urlpatterns = [
    path('list', VideoView.as_view()),
]