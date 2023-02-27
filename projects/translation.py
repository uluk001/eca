from modeltranslation.translator import TranslationOptions, register
from .models import Project

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name_of_client', 'financing_agency', 'country', 'sector', 'month','projects_detail')
