from django import forms

from appsocio.models import Socio

class buscarSocioForm(forms.Form):
    codigo = forms.ModelChoiceField(label='Codigo de Usuario', queryset=Socio.objects.all())