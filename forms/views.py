from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from forms.models import Contact, Resume
from forms.serializers import ContactSerializer, ResumeSerializer
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import views


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


class CreateResumeView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]