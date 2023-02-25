from django.contrib import admin
from .models import Members

class MembersAdmin(admin.ModelAdmin):
    list_display = ('ecas_role', )

admin.site.register(Members, MembersAdmin)