from django.contrib import admin
from .models import *

class RefugeeAdminModel(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'father_name', 'birth_date', 'id_serial', 'fin', 'city'
    list_filter = 'first_name', 'last_name', 'father_name', 'birth_date', 'id_serial', 'fin', 'city'

admin.site.register([Country, City])
admin.site.register(Refugee, RefugeeAdminModel)
