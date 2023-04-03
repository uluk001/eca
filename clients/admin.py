from django.contrib import admin
from .models import Category, OurClients, PartnerImage


admin.site.register(Category)
admin.site.register(PartnerImage)
admin.site.register(OurClients)