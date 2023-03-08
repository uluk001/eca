from .models import Category, OurClients
from .serializers import *
from rest_framework import generics

class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class OurClientsView(generics.ListAPIView):
    """
    Передаете {id}
    """
    serializer_class = OurClientsSerializer

    def get_queryset(self):
        category = Category.objects.get(id = self.kwargs['id'])
        queryset = OurClients.objects.filter(category=category)
        return queryset


class OurClientsListView(generics.ListAPIView):

    serializer_class = OurClientsSerializer
    queryset = OurClients.objects.all()
