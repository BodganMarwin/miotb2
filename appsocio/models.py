from django.db import models

# Create your models here.

departamentos = [
    ('La Paz','Lp'),
    ('Oruro','Or'),
    ('Potosi','Pt'),
    ('Cochabamba','Cbba'),
    ('Chuquisaca','Ch'),
    ('Tarija','Tj'),
    ('Santa Cruz','Sc'),
    ('Beni','Bn'),
    ('Pando','Pn'),
]

class Socio(models.Model):
    codigo = models.CharField(max_length=8,unique=True, verbose_name='Codigo Socio')
    nombre = models.CharField(max_length=20, verbose_name='Nombre Socio')
    apellido = models.CharField(max_length=50, verbose_name='Apellidos Socio')
    ci = models.PositiveIntegerField(null=True,blank=True, verbose_name='Cedula de Identidad')
    expedito = models.CharField(max_length=10,choices=departamentos,null=True,blank=True)
    telefono = models.PositiveIntegerField(null=True,blank=True, verbose_name='Telefono Fijo')
    celular = models.PositiveIntegerField(null=True,blank=True)
    direccion = models.TextField(null=True,blank=True, verbose_name='Direccion del Socio')
    estado = models.BooleanField(null=True,blank=True, verbose_name='Activar')

    def __str__(self):
        return self.codigo+' '+self.nombre+' '+self.apellido

    class Meta:
        managed = True
        db_table = 'socio'
