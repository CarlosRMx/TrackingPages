from django.contrib import admin

from .models import Client, Package, Administrator


# Register your models here.

admin.site.register(Client)
admin.site.register(Package)
admin.site.register(Administrator)
