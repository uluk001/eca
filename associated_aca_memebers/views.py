from .serializers import MembersSerializer
from .models import Members
from rest_framework.generics import ListAPIView

class MembersView(ListAPIView):
    serializer_class = MembersSerializer
    queryset = Members.objects.all()
 