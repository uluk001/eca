from rest_framework import serializers
from .models import Category, OurClients

# Ru

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class OurClientsSerializer(serializers.ModelSerializer):

    content = serializers.SerializerMethodField()
    content_ru = serializers.SerializerMethodField()
    content_en = serializers.SerializerMethodField()

    class Meta:
        model = OurClients
        fields = '__all__'



    def get_content(self, obj):
        return str(obj.content.html)
    
    def get_content_ru(self, obj):
        return str(obj.content_ru.html)
    
    def get_content_en(self, obj):
        return str(obj.content_en.html)