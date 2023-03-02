from django.urls import path, re_path
from .views import CategoryView, OurClientsView


urlpatterns = [

    path('ru/category_list/', CategoryView.as_view()),
    re_path('ru/retrieve/(?P<id>.+)/$', OurClientsView.as_view()),

]
