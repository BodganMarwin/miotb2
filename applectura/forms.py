from django import forms

from appsocio.models import Socio
from applectura.models import Lectura

# class buscarSocioForm(forms.ModelForm):
#     codigo = forms.ModelChoiceField(label='Codigo de Usuario', 
#                                     queryset=Socio.objects.all(),
#                                     widget=forms.Select({
#                                         'class':'form-select'
#                                     }))

class buscarSocioForm(forms.Form):
    codigo = forms.CharField(max_length=8,label='Codigo de Usuario:',widget=forms.TextInput(attrs={'class':'form-control'}))

class realizarLecturaForm(forms.Form):
    anterior = forms.CharField(max_length=10,label='Lectura del mes Anterior:',
                               widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'disabled':'true'
                               }))
    actual = forms.FloatField(label='Lectura Actual:',
                              widget=forms.TextInput(attrs={
                                   'class':'form-control'
                               }))
    fechaemision = forms.DateField(label='Fecha de Emision:',
                            widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'disabled':'true'
                               }))
    mes = forms.CharField(label='Periodo de Emision:',
                          widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'disabled':'true'
                               }))
    anio = forms.CharField(label='Gestion de Emision:',
                           widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'disabled':'true'
                               }))
    multa = forms.CharField(label='Multa por Mora:',
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'disabled':'true'
                            }))
    socio = forms.CharField(label='Socio:',
                           widget=forms.TextInput(attrs={
                                   'class':'form-control',
                                   'disabled':'true'
                               }))
    # class Meta:
    #     model=Lectura
    #     fields=('anterior','actual','fecha','mes','anio','socio')

class LecturaForm(forms.ModelForm):
    class Meta:
        model = Lectura
        fields = '__all__'
        # fields=('anterior','actual','consumo','pagoconsumo','multa','pagototal','fecha','mes','anio','estado','socio')

class CobrarLecturaForm(forms.ModelForm):
    class Meta:
        model = Lectura
        fields = '(__all__)'
        fields = ('anterior','actual','consumo','pagoconsumo','multa','pagototal','fechaemision','mes','anio','estado','socio')
        widgets = {
            'anterior': forms.NumberInput(attrs={'class':'form-control','disabled':True}),
            'actual': forms.NumberInput(attrs={'class':'form-control','disabled':True}),
            'consumo': forms.NumberInput(attrs={'class':'form-control','disabled':True}),
            'pagoconsumo': forms.NumberInput(attrs={'class':'form-control','disabled':True}),
            'multa': forms.NumberInput(attrs={'class':'form-control','disabled':True}),
            'pagototal': forms.NumberInput(attrs={'class':'form-control','disabled':True}),
            'fechaemision': forms.DateInput(attrs={'class':'form-control','disabled':True}),
            # 'fechapago': forms.DateInput(attrs={'class':'form-control','disabled':True}),
            'mes': forms.TextInput(attrs={'class':'form-control','disabled':True}),
            'anio': forms.NumberInput(attrs={'class':'form-control','disabled':True}),
            'estado': forms.NullBooleanSelect(attrs={'class':'form-control','disabled':True}),
            'socio': forms.Select(attrs={'class':'form-control','disabled':True}),
        } 

class PrimeraLecturaForm(forms.ModelForm):
    class Meta:
        model = Lectura
        fields = ('actual','fechaemision')
        widgets = {
            'actual': forms.TextInput(attrs={'class':'form-control'}),
            'fechaemision': forms.DateInput(attrs={'class':'form-control', 'disabled':True}),
        }