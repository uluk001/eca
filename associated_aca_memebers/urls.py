from django.urls import path
from .views import MembersView, MembersViewEn


urlpatterns = [
    # ru
    path('ru/list/', MembersView.as_view()),

    # en
    path('en/list/', MembersViewEn.as_view()),
]
