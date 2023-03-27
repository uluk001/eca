from rest_framework import generics
from .serializers import VideoSerializer
from .models import Video


# Projects list
class VideoView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

