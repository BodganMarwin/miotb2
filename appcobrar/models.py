from django.db import models
from applectura.models import Lectura

# Create your models here.

class Cobrar(models.Model):
    fecha = models.DateField(verbose_name='Fecha de Cobro')
    lectura = models.ForeignKey(Lectura, verbose_name='Lectura', on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'cobrar'
