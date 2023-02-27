from rest_framework.serializers import ModelSerializer
from .models import Category, OurClients

# Ru

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class OurClientsSerializer(ModelSerializer):

    class Meta:
        model = OurClients
        fields = '__all__'

# En

class CategorySerializerEn(ModelSerializer):

    class Meta:
        model = Category
        fields = ('title_en',)


class OurClientsSerializerEn(ModelSerializer):

    class Meta:
        model = OurClients
        fields = ('сompany_name_en', 'content_en', 'image', 'category')