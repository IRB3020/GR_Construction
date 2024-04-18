from django.contrib import admin
from .models import Client, Bill, WorkSite

# Register your models here.
admin.site.register(Client)
admin.site.register(Bill)
admin.site.register(WorkSite)
