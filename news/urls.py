from django.urls import path, re_path
from news.views import NewsListView, NewsRetrieveView, LatestNews, NewImagesView, NewsYearsList, NewsByYear


urlpatterns = [
    # ru
    path('latest/', LatestNews.as_view()),
    path('list/', NewsListView.as_view()),
    path('retreive/<pk>', NewsRetrieveView.as_view()),
    path('list_of_years/', NewsYearsList.as_view()),
    re_path('news_by_year/(?P<year>.+)/$', NewsByYear.as_view()),

    # images
    re_path('images/(?P<id>.+)/$', NewImagesView.as_view()),
]
