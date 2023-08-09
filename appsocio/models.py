from django.db import models
from django.contrib.gis.db import models

# Create your models here.

departamentos = [
    ('Lp','Lp'),
    ('Or','Or'),
    ('Pt','Pt'),
    ('Cbba','Cbba'),
    ('Ch','Ch'),
    ('Tj','Tj'),
    ('Sc','Sc'),
    ('Bn','Bn'),
    ('Pn','Pn'),
]

class Socio(models.Model):
    codigo = models.CharField(max_length=8,unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    ci = models.PositiveIntegerField(null=True,blank=True)
    expedito = models.CharField(max_length=10,choices=departamentos,null=True,blank=True)
    telefono = models.PositiveIntegerField(null=True,blank=True)
    celular = models.PositiveIntegerField(null=True,blank=True)
    direccion = models.TextField(null=True,blank=True)
    estado = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.codigo+' '+self.nombre+' '+self.apellido

    class Meta:
        managed = True
        db_table = 'socio'
