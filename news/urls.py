from django.urls import path
from news.views import NewsListView, NewsRetrieveView, LatestNews


urlpatterns = [
    path('list/', NewsListView.as_view()),
    path('latest/', LatestNews.as_view()),
    path('retreive/<pk>', NewsRetrieveView.as_view()),
]