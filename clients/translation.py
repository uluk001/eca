from modeltranslation.translator import TranslationOptions, register
from .models import *

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(OurClients)
class OurClientsTranslationOptions(TranslationOptions):
    fields = ('сompany_name', 'content')