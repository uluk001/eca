from rest_framework import serializers
from django_quill.fields import FieldQuill
from rest_framework.serializers import ModelSerializer
from projects.models import Project


class ProjectSerializer(ModelSerializer):

    projects_detail = serializers.SerializerMethodField()
    projects_detail_ru = serializers.SerializerMethodField()
    projects_detail_en = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'


    def get_projects_detail(self, obj):
        return str(obj.projects_detail.html)

    def get_projects_detail_ru(self, obj):
        return str(obj.projects_detail_ru.html)
    
    def get_projects_detail_en(self, obj):
        return str(obj.projects_detail_en.html)