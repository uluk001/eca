from django.urls import path
from .views import MembersView


urlpatterns = [
    path('list/', MembersView.as_view()),
]
