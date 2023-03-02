from rest_framework import serializers
from .models import Members

class MembersSerializer(serializers.ModelSerializer):

    discription = serializers.SerializerMethodField()
    discription_ru = serializers.SerializerMethodField()
    discription_en = serializers.SerializerMethodField()

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

    def get_discription(self, obj):
        return str(obj.discription.html)
    
    def get_discription_ru(self, obj):
        return str(obj.discription_ru.html)
    
    def get_discription_en(self, obj):
        return str(obj.discription_en.html)