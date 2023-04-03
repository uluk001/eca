from django.contrib import admin
from .models import Members, EcasRole

class EcasRoleInline(admin.TabularInline):
    model= EcasRole

@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    inlines = [EcasRoleInline]