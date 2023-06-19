from django.contrib import admin
from apptroncal.models import Cliente, Servicio, Georeferencias

# Register your models here.

admin.site.register(Georeferencias)
admin.site.register(Cliente)
admin.site.register(Servicio)