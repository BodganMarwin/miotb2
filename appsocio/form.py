from django import forms
from .models import *

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ('nombre','apellido','ci','expedito','telefono','celular','direccion')
        labels = {
            'nombre':'Nombre de Socio:',
            'apellido': 'Apellido de Socio:',
            'ci': 'Cedula de Identidad:',
            'expedito': 'Expedito:',
            'telefono': 'Número de Telefono Fijo',
            'celular': 'Número de Celular:',
            'direccion': 'Direción de Socio:'
        }
        widgets = {
            # 'codigo': forms.TextInput(attrs={'class':'form-control','placeholder':'Codigo'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'ci': forms.NumberInput(attrs={'class':'form-control'}),
            'expedito': forms.Select(attrs={'class':'form-select'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
            'celular': forms.NumberInput(attrs={'class':'form-control'}),
            'direccion': forms.Textarea(attrs={'class':'form-control'}),
            # 'estado': forms.Select(attrs={'class':'form-control'}),
        }