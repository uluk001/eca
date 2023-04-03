from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
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


# class CreateResumeView(generics.CreateAPIView):
#     queryset = Resume.objects.all()
#     serializer_class = ResumeSerializer
    

class CreateResumeView(APIView):
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request, format=None):
        """
        curl -X POST -S \
          -H 'Accept: application/json' \
          -H 'Content-Type: multipart/form-data' \
          -F "first_name={first_name}" \
          -F "last_name={last_name}" \
          -F "email={email}" \
          -F "name={}" \
          -F "resume=@/path/to/your_photo.jpg;type=type of your file" \
          http://127.0.0.1:9000/forms/resume/
        """
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                first_name=request.data.get('first_name'),
                last_name=request.data.get('last_name'),
                email=request.data.get('email'),
                resume=request.data.get('resume')
            )
            return Response({'reply':'Your Resume / CV was successfully sent. Our staff will contact you as soon as possible'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)