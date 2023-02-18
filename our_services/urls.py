from django.urls import path, re_path
from .views import ServicesIncludeView, ServicesListView


urlpatterns = [
    path('list/', ServicesListView.as_view()),
    re_path('filter_by_service/(?P<id>.+)/$', ServicesIncludeView.as_view()),
]