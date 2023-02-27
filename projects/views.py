from rest_framework import generics
from .serializers import *
from .models import *


# Projects list
class ProjectListViewRu(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerRu


# List of years
class ListOfYearsViewRu(generics.ListAPIView):
    serializer_class = ProjectSerializerRu

    def get_queryset(self):
        return Project.objects.all().values('year')



# Searcher
class SearchProjectRu(generics.ListAPIView):
    serializer_class = ProjectSerializerRu

    def get_queryset(self):
        return Project.objects.filter(name_of_client__contains=self.kwargs['name'])


# Filter by year 
class FilterByYearRu(generics.ListAPIView):
    serializer_class = ProjectSerializerRu

    def get_queryset(self):
        year = self.kwargs['year']
        return Project.objects.filter(year=year)


# Filter by sector 
class FilterBySectorRu(generics.ListAPIView):
    serializer_class = ProjectSerializerRu

    def get_queryset(self):
        sector = self.kwargs['sector']
        return Project.objects.filter(sector=sector)


# Projects list
class ProjectListViewEn(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerEn


# List of years
class ListOfYearsViewEn(generics.ListAPIView):
    serializer_class = ProjectSerializerEn

    def get_queryset(self):
        return Project.objects.all().values('year')



# Searcher
class SearchProjectEn(generics.ListAPIView):
    serializer_class = ProjectSerializerEn

    def get_queryset(self):
        return Project.objects.filter(name_of_client__contains=self.kwargs['name'])


# Filter by year 
class FilterByYearEn(generics.ListAPIView):
    serializer_class = ProjectSerializerEn

    def get_queryset(self):
        year = self.kwargs['year']
        return Project.objects.filter(year=year)


# Filter by sector 
class FilterBySectorEn(generics.ListAPIView):
    serializer_class = ProjectSerializerEn

    def get_queryset(self):
        sector = self.kwargs['sector']
        return Project.objects.filter(sector=sector)