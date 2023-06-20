from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Georeferencias(models.Model):
    punto = models.PointField(srid=4326, blank=True, null=True)
    # linea = models.LineStringField(srid=4326, blank=True, null=True)
    poligono = models.PolygonField(srid=4326, blank=True, null=True)
    multipunto = models.MultiPointField(srid=4326, blank=True, null=True)
    # multilinea= models.MultiLineStringField(srid=4326, blank=True, null=True)
    multipoligono = models.MultiPolygonField(srid=4326, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'georefencia'

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'servicio'

gen = [('Masculino','MASCULINO'),('Femenino','FEMENINO')]

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=10,choices=gen)
    tipoMedalla = models.TextChoices('tipoMedalla', 'GOLD SILVER BRONZE')
    medalla = models.CharField(choices=tipoMedalla.choices, max_length=10)
    ci = models.IntegerField()
    servicio = models.ForeignKey(Servicio, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre+' '+self.apellido

    class Meta:
        managed = True
        db_table = 'cliente'


