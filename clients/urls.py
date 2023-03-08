from django.urls import path, re_path
from .views import CategoryView, OurClientsView, OurClients


urlpatterns = [

    path('category_list/', CategoryView.as_view()),
    re_path('retrieve/(?P<id>.+)/$', OurClientsView.as_view()),
    path('list/', OurClientsView.as_view()),
]
