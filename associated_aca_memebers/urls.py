from django.urls import path, re_path
from .views import MembersView, EcasRoleView


urlpatterns = [
    path('list/', MembersView.as_view()),
    re_path('ecas_role/(?P<id>.+)/$', EcasRoleView.as_view()),
]
