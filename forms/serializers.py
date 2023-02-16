from rest_framework.serializers import ModelSerializer
from forms.models import Contact, Resume

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ResumeSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'