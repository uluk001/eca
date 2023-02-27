from django.urls import path, re_path
from .views import CategoryView, OurClientsView, CategoryViewEn, OurClientsViewEn


urlpatterns = [
    # ru
    path('ru/category_list/', CategoryView.as_view()),
    re_path('ru/retrieve/(?P<id>.+)/$', OurClientsView.as_view()),

    # en
    path('en/category_list/', CategoryViewEn.as_view()),
    re_path('en/retrieve/(?P<id>.+)/$', OurClientsViewEn.as_view()),
]
