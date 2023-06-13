from django.db import models
from appsocio.models import Socio

# Create your models here.

meses = [
    ('ENERO','ENERO'),
    ('FEBRERO','FEBRERO'),
    ('MARZO','MARZO'),
    ('ABRIL','ABRIL'),
    ('MAYO','MAYO'),
    ('JUNIO','JUNIO'),
    ('JULIO','JULIO'),
    ('AGOSTO','AGOSTO'),
    ('SEPTIEMBRE','SEPTIEMBRE'),
    ('OCTUBRE','OCTUBRE'),
    ('NOVIEMBRE','NOVIEMBRE'),
    ('DICIEMBRE','DICIEMBRE')]
anios = [('2022','2022'),('2023','2023'),('2024','2024')]

class Lectura(models.Model):
    anterior = models.FloatField(verbose_name='Lectura Anterior')
    actual = models.FloatField(verbose_name='Lectura Actual')
    consumo = models.FloatField(verbose_name='Consumo en m3')
    pagoconsumo = models.FloatField(verbose_name='Monto de Consumo')
    multa = models.FloatField(verbose_name='Multa Varios')
    pagototal = models.FloatField(verbose_name='Monto total a pagar')
    fecha = models.DateField(verbose_name='Fecha de Emision',null=True,blank=True)
    mes = models.CharField(max_length=10,choices=meses,verbose_name='Periodo')
    anio = models.CharField(choices=anios, max_length=4, verbose_name='Gestion')
    estado = models.BooleanField(null=True,blank=True, verbose_name='Pagado')
    socio = models.ForeignKey(Socio, on_delete=models.RESTRICT)

    def __str__(self):
        return self.anio+' '+self.mes+' '+self.socio.codigo

    class Meta:
        managed = True
        db_table = 'lectura'
    