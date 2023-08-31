from django import forms
from .models import *

class CobrarForm(forms.ModelForm):
    class Meta:
        models = Cobrar
        fields = '__all__'