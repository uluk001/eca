from django.urls import path, re_path
from news.views import NewsListView, NewsRetrieveView, LatestNews, NewImagesView


urlpatterns = [
    # ru
    path('latest/', LatestNews.as_view()),
    path('list/', NewsListView.as_view()),
    path('retreive/<pk>', NewsRetrieveView.as_view()),

    # images
    re_path('images/(?P<id>.+)/$', NewImagesView.as_view()),
]
