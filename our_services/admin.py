from django.contrib import admin
from .models import Services, ServicesInclude

class ServicesIncludeInline(admin.TabularInline):
    model = ServicesInclude

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    inlines = [ServicesIncludeInline]
    list_display = ('title',)
