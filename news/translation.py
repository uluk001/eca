from modeltranslation.translator import TranslationOptions, register
from .models import *

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
