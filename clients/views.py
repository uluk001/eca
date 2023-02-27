from .models import Category, OurClients
from .serializers import *
from rest_framework import generics

# Ru 

class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class OurClientsView(generics.ListAPIView):
    """
    Передаете {id}
    """
    serializer_class = OurClientsSerializer

    def get_queryset(self):
        category = Category.objects.get(id = self.request.kwargs['id'])
        queryset = OurClients.objects.filter(category=category)
        return queryset

# En

class CategoryViewEn(generics.ListAPIView):
    serializer_class = CategorySerializerEn
    queryset = Category.objects.all()


class OurClientsViewEn(generics.ListAPIView):
    """
    Передаете {id}
    """
    serializer_class = OurClientsSerializerEn

    def get_queryset(self):
        category = Category.objects.get(id = self.request.kwargs['id'])
        queryset = OurClients.objects.filter(category=category)
        return queryset