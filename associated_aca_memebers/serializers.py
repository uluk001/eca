from rest_framework import serializers
from .models import Members, EcasRole



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
    
class MembersSerializer(serializers.ModelSerializer):
    ecas_roles = EcasRoleSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()
    description_ru = serializers.SerializerMethodField()
    description_en = serializers.SerializerMethodField()

    class Meta:
        model = Members
        fields = '__all__'

    @classmethod
    def setup_eager_loading(cls, queryset):
        queryset = queryset.prefetch_related('ecas_roles')
        return queryset

    def get_description(self, obj):
        return str(obj.description.html)
    
    def get_description_ru(self, obj):
        return str(obj.description_ru.html)
    
    def get_description_en(self, obj):
        return str(obj.description_en.html)
    
