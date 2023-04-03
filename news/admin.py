from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)

class NewImageAdmin(admin.ModelAdmin):
    list_display = ('news',)

admin.site.register(News, NewsAdmin)
admin.site.register(NewImages, NewImageAdmin)