from rest_framework.serializers import ModelSerializer
from projects.models import Project



class ProjectSerializerEn(ModelSerializer):
    class Meta:
        model = Project
        fields = ('name_of_client_en', 'financing_agency_en', 'country_en', 'sector_en', 'month_en','year','projects_detail_en','client')

class ProjectSerializerRu(ModelSerializer):
    class Meta:
        model = Project
        fields = ('name_of_client_ru', 'financing_agency_ru', 'country_ru', 'sector_ru', 'month_ru','year','projects_detail_ru','client')
