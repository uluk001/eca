from modeltranslation.translator import TranslationOptions, register
from .models import *

@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ServicesInclude)
class ServicesIncludeTranslationOptions(TranslationOptions):
    fields = ('denotation',)
