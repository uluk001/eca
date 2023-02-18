from django.urls import path, re_path
from projects.views import SearchProject, ProjectListView, FilterByYear, FilterBySector


urlpatterns = [
    re_path('search/(?P<name>.+)/$', SearchProject.as_view()),
    re_path('filter_by_sector/(?P<sector>.+)/$', FilterBySector.as_view()),
    re_path('filter_by_year/(?P<year>.+)/$', FilterByYear.as_view()),
    path('list', ProjectListView.as_view()),
]