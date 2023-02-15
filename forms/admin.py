from django.contrib import admin
from forms.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Contact, ContactAdmin)