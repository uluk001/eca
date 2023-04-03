from django.urls import path
from forms.views import CreateContactView, CreateResumeView


urlpatterns = [
    path('contact/', CreateContactView.as_view()),
    path('resume/', CreateResumeView.as_view()),
]