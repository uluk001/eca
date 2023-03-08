from modeltranslation.translator import TranslationOptions, register
from .models import *

@register(Members)
class MembersTranslationOptions(TranslationOptions):
    fields = ('description', 'ecas_role')
