from rest_framework import generics
from .serializers import *
from .models import *


# Projects list
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# List of years
class ListOfYearsView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all().values('year')



# Searcher
class SearchProject(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(name_of_client__contains=self.kwargs['name'])


# Filter by year 
class FilterByYear(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        return Project.objects.filter(year=year)


# Filter by sector 
class FilterBySector(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        sector = self.kwargs['sector']
        return Project.objects.filter(sector=sector)

