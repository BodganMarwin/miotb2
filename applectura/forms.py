from django import forms

from appsocio.models import Socio
from applectura.models import Lectura

class buscarSocioForm(forms.Form):
    codigo = forms.ModelChoiceField(label='Codigo de Usuario', 
                                    queryset=Socio.objects.all(),
                                    widget=forms.Select({
                                        'class':'form-select'
                                    }))

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
    fecha = forms.DateField(label='Fecha de Emision:',
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

class PrimeraLecturaForm(forms.ModelForm):
    class Meta:
        model = Lectura
        fields = ('actual','fecha')
        widgets = {
            'actual': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control', 'disabled':True}),
        }