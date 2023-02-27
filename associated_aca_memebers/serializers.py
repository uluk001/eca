from rest_framework import serializers
from .models import Members

# ru 
class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

# en
class MembersSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('discription_en', 'image', 'ecas_role_en')