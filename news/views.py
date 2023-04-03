from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from .paginators import CustomPagination
# Create your views here.

# Ru 

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
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
