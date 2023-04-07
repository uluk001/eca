from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from .paginators import CustomPagination
from django.db.models.functions import ExtractYear
# Create your views here.


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


class NewsRetrieveView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class LatestNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all().order_by('-created_at')[:3]


class NewImagesView(generics.ListAPIView):
    serializer_class = NewImagesSerializer

    def get_queryset(self):
        news = News.objects.get(id=self.kwargs['id'])
        return NewImages.objects.filter(news=news)
    


class NewsYearsList(APIView):
    def get(self, request):
        years_list = News.objects.annotate(year=ExtractYear('created_at')).values('year').annotate(total=Count('id')).order_by('-year')
        return Response(years_list)
    
class NewsByYear(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.filter(created_at__year=self.kwargs['year'])