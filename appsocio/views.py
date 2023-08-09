from typing import Any
from django import http
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import *
from .models import Socio
from .form import SocioForm

# Create your views here.

class ListarSociosView(ListView):
    model = Socio
    template_name = 'socio/listarsocios.html'
    context_object_name = 'socios'
    paginate_by = 10
    
class CrearSocioView(CreateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socio/crearsocio.html'
    success_url = reverse_lazy('listarsocios')

class EditarSocioView(UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socio/crearsocio.html'
    success_url = reverse_lazy('listarsocios')

class EliminarSocioView(DeleteView):
    model = Socio
    template_name = 'socio/eliminarSocio.html'
    success_url = reverse_lazy('listarsocios')
    