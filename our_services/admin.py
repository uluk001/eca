from django.contrib import admin
from .models import Services, ServicesInclude

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ServicesIncludeAdmin(admin.ModelAdmin):
    list_display = ('service', 'denotation')

admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesInclude, ServicesIncludeAdmin)