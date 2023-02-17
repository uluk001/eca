from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsRetrieveView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer