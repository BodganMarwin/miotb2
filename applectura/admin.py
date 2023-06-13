from django.contrib import admin
from applectura.models import Lectura
# Register your models here.

class LecturaAdmin(admin.ModelAdmin):
    list_display = ('mes','anio','consumo','pagoconsumo','pagototal','socio')
    ordering = ['anio','mes']
    list_filter = ['estado']

admin.site.register(Lectura,LecturaAdmin)