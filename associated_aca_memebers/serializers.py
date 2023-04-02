from rest_framework import serializers
from .models import Members, EcasRole

class MembersSerializer(serializers.ModelSerializer):

    description = serializers.SerializerMethodField()
    description_ru = serializers.SerializerMethodField()
    description_en = serializers.SerializerMethodField()

    class Meta:
        model = Members
        fields = '__all__'

    def get_description(self, obj):
        return str(obj.description.html)
    
    def get_description_ru(self, obj):
        return str(obj.description_ru.html)
    
    def get_description_en(self, obj):
        return str(obj.description_en.html)
    

    
class EcasRoleSerializer(serializers.ModelSerializer):

    title = serializers.SerializerMethodField()
    title_ru = serializers.SerializerMethodField()
    title_en = serializers.SerializerMethodField()

    class Meta:
        model = EcasRole
        fields = '__all__'

    def get_title(self, obj):
        return str(obj.title.html)
    
    def get_title_ru(self, obj):
        return str(obj.title_ru.html)
    
    def get_title_en(self, obj):
        return str(obj.title_en.html)