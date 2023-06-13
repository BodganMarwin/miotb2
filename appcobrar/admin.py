from django.contrib import admin
from appcobrar.models import Cobrar

# Register your models here.

class CobrarAdmin(admin.ModelAdmin):
    list_display = ('fecha','lectura')

admin.site.register(Cobrar, CobrarAdmin)
