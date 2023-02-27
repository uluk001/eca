from django.urls import path, re_path
from .views import ServicesIncludeView, ServicesListView, ServicesRetrieveView, ServicesIncludeViewEn, ServicesListViewEn, ServicesRetrieveViewEn


urlpatterns = [
    # ru
    path('ru/list/', ServicesListView.as_view()),
    re_path('ru/service_retrieve/(?P<id>.+)/$', ServicesRetrieveView.as_view()),
    re_path('ru/filter_by_service/(?P<id>.+)/$', ServicesIncludeView.as_view()),
    
    # en
    path('en/list/', ServicesListViewEn.as_view()),
    re_path('en/service_retrieve/(?P<id>.+)/$', ServicesRetrieveViewEn.as_view()),
    re_path('en/filter_by_service/(?P<id>.+)/$', ServicesIncludeViewEn.as_view()),
]