from django.urls import path, re_path
from .views import CategoryView, OurClientsView, OurClientsListView, PartnerImageListView


urlpatterns = [

    path('category_list/', CategoryView.as_view()),
    re_path('retrieve/(?P<id>.+)/$', OurClientsView.as_view()),
    path('list/', OurClientsListView.as_view()),
    path('partner_image_list/', PartnerImageListView.as_view()),
]
