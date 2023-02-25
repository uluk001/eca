from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

class ServicesListView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesIncludeView(generics.ListAPIView):
    serializer_class = ServicesIncludeSerializer

    def get_queryset(self):
        service = Services.objects.get(id=self.kwargs['id'])
        return ServicesInclude.objects.filter(service=service)


class ServicesRetrieveView(generics.ListAPIView):
    serializer_class = ServicesSerializer

    def get_queryset(self):
        service = Services.objects.get(id=self.kwargs['id'])
        return service
