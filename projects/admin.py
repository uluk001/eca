from django.contrib import admin
from projects.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name_of_client',)

admin.site.register(Project, ProjectAdmin)