from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from forms.models import Contact
from forms.serializers import ContactSerializer
# Create your views here.

# class ContactView(ModelViewSet):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     permission_classes = [IsAuthenticated]
#     def create(self, request):
#         pass


class CreateContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]