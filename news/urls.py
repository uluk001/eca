from django.urls import path, re_path
from news.views import NewsListView, NewsRetrieveView, LatestNews, NewImagesView


urlpatterns = [
    # ru
    path('ru/list/', NewsListView.as_view()),
    path('ru/latest/', LatestNews.as_view()),
    path('ru/retreive/<pk>', NewsRetrieveView.as_view()),

    # en
    path('en/list/', NewsListView.as_view()),
    path('en/latest/', LatestNews.as_view()),
    path('en/retreive/<pk>', NewsRetrieveView.as_view()),

    # images
    re_path('images/(?P<id>.+)/$', NewImagesView.as_view()),
]
