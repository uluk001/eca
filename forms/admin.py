from django.contrib import admin
from forms.models import Contact, Resume
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Resume, ResumeAdmin)