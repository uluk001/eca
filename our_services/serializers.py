from rest_framework.serializers import ModelSerializer
from .models import Services, ServicesInclude

class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class ServicesIncludeSerializer(ModelSerializer):
    class Meta:
        model = ServicesInclude
        fields = '__all__'