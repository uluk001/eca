from django.urls import path, re_path
from .views import MembersView, EcasRoleList


urlpatterns = [
    path('list/', MembersView.as_view()),
    re_path('role/(?P<id>.+)/$', EcasRoleList.as_view()),
]
