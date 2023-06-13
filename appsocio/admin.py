from django.contrib import admin
from appsocio.models import Socio

# Register your models here.
class SocioAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','apellido','ci','direccion')
    ordering = ['codigo']

admin.site.register(Socio,SocioAdmin)
