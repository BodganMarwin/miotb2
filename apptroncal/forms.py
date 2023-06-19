from django import forms
from apptroncal.models import Georeferencias, Cliente, Servicio

class GeoForm(forms.ModelForm):
    class Meta:
        model = Georeferencias
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'