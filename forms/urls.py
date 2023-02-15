from django.urls import path
from forms.views import CreateContactView


urlpatterns = [
    path('contact/', CreateContactView.as_view()),
]
