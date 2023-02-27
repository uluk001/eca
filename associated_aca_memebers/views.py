from .serializers import MembersSerializer, MembersSerializerEn
from .models import Members
from rest_framework.generics import ListAPIView

# Ru
class MembersView(ListAPIView):
    serializer_class = MembersSerializer
    queryset = Members.objects.all()

# En
class MembersViewEn(ListAPIView):
    serializer_class = MembersSerializerEn
    queryset = Members.objects.all()