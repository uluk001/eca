from rest_framework import serializers
from .models import Services, ServicesInclude

class ServicesSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    description_ru = serializers.SerializerMethodField()
    description_en = serializers.SerializerMethodField()

    class Meta:
        model = Services
        fields = '__all__'

    def get_description(self, obj):
        return str(obj.description.html)
    
    def get_description_ru(self, obj):
        return str(obj.description_ru.html)
    
    def get_description_en(self, obj):
        return str(obj.description_en.html)

class ServicesIncludeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesInclude
        fields = '__all__'