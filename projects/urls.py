from django.urls import path, re_path
from projects.views import SearchProjectEn, ProjectListViewEn, FilterByYearEn, FilterBySectorEn, SearchProjectRu, FilterBySectorRu, ListOfYearsViewRu, FilterByYearRu, ProjectListViewRu, ListOfYearsViewEn


urlpatterns = [
    # en
    re_path('en/search/(?P<name>.+)/$', SearchProjectEn.as_view()),
    re_path('en/filter_by_sector/(?P<sector>.+)/$', FilterBySectorEn.as_view()),
    re_path('en/filter_by_year/(?P<year>.+)/$', FilterByYearEn.as_view()),
    path('en/list', ProjectListViewEn.as_view()),
    path('en/list_of_years', ListOfYearsViewEn.as_view()),

    # ru
    re_path('ru/search/(?P<name>.+)/$', SearchProjectRu.as_view()),
    re_path('ru/filter_by_sector/(?P<sector>.+)/$', FilterBySectorRu.as_view()),
    re_path('ru/filter_by_year/(?P<year>.+)/$', FilterByYearRu.as_view()),
    path('ru/list', ProjectListViewRu.as_view()),
    path('ru/list_of_years', ListOfYearsViewRu.as_view()),
]