from rest_framework.serializers import ModelSerializer
from forms.models import Contact

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'