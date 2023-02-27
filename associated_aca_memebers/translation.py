from modeltranslation.translator import TranslationOptions, register
from .models import *

@register(Members)
class MembersTranslationOptions(TranslationOptions):
    fields = ('discription', 'ecas_role')
