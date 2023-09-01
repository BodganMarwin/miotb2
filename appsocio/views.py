from typing import Any
from django import http
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import *
from .models import Socio
from .form import SocioForm

# Create your views here.

class ListarSociosView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'appsocio.view_socio'
    model = Socio
    template_name = 'socio/listarsocios.html'
    context_object_name = 'socios'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        socios = Socio.objects.filter(estado=True)
        return render(request,self.template_name,{'socios':socios, 'tipo':'Socio', 'subtipo':'Ver Socios','accion':'Socios'})
    
class CrearSocioView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'appsocio.add_socio'
    model = Socio
    form_class = SocioForm
    template_name = 'socio/socio.html'
    success_url = reverse_lazy('listarsocios')
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any):
        form = self.form_class(request.POST)
        if form.is_valid():
            socios = Socio.objects.all()
            if socios:
                socio = socios.last()
                if socio.id < 9:
                    codigo = 'SUCA-00'+str(socio.id+1)
                elif socio.id < 99:
                    codigo = 'SUCA-0'+str(socio.id+1)
                else:
                    codigo = 'SUCA-'+str(socio.id+1)
            else: 
                codigo = 'SUCA-001'
            socio = Socio(
                codigo = codigo,
                nombre = (form.cleaned_data['nombre']).upper(),
                apellido = (form.cleaned_data['apellido']).upper(),
                ci = form.cleaned_data['ci'],
                expedito = form.cleaned_data['expedito'],
                telefono = form.cleaned_data['telefono'],
                celular = form.cleaned_data['celular'],
                direccion = (form.cleaned_data['direccion']).upper(),
                estado = True,
            )
            print(socio.nombre)
            socio.save()
            return redirect('listarsocios')
        return render(request, self.template_name,{'form':self.form_class})

class EditarSocioView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'appsocio.update_socio'
    model = Socio
    form_class = SocioForm
    template_name = 'socio/crearsocio.html'
    success_url = reverse_lazy('listarsocios')

class EliminarSocioView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'appsocio.delete_socio'
    model = Socio
    template_name = 'socio/eliminarSocio.html'
    success_url = reverse_lazy('listarsocios')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estado = False
        self.object.save()
        return redirect(self.success_url)
    