from rest_framework import serializers
from .models import Members

class MembersSerializer(serializers.ModelSerializer):

    description = serializers.SerializerMethodField()
    description_ru = serializers.SerializerMethodField()
    description_en = serializers.SerializerMethodField()

    ecas_role = serializers.SerializerMethodField()
    ecas_role_ru = serializers.SerializerMethodField()
    ecas_role_en = serializers.SerializerMethodField()

    class Meta:
        model = Members
        fields = '__all__'

    def get_ecas_role(self, obj):
        return str(obj.ecas_role.html)
    
    def get_ecas_role_ru(self, obj):
        return str(obj.ecas_role_ru.html)
    
    def get_ecas_role_en(self, obj):
        return str(obj.ecas_role_en.html)

    def get_description(self, obj):
        return str(obj.description.html)
    
    def get_description_ru(self, obj):
        return str(obj.description_ru.html)
    
    def get_description_en(self, obj):
        return str(obj.description_en.html)