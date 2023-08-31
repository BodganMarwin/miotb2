from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView,UpdateView
from django.shortcuts import render
from applectura.forms import *
from applectura.views import *
from applectura.models import *
from .models import *
from .forms import *

# Create your views here.

def buscarSocioCobrar(request):
    form = buscarSocioForm()
    mes = mesAnterior(date.today().month)
    anio = anioMes(date.today().month)
    try:
        # lecturasSinpagar = Lectura.objects.filter(estado=False,anio=anio,mes=mes)
        alllecturasSinpagar = Lectura.objects.filter(anterior__gt=0,estado=False)
    except Lectura.DoesNotExist:
        alllecturasSinpagar = None
    if request.method == 'POST':
        form = buscarSocioForm(request.POST)
        if form.is_valid:
            id = request.POST['codigo']
            socio = Socio.objects.get(id=id)
            try:
                lecturasSinpagar = Lectura.objects.filter(anterior__gt=0,socio=socio,estado=False)
                return render(request, 'lecturassinpagar.html',{'objetos':lecturasSinpagar,'socio':socio, 'tipo':'Cobrar','subtipo':'Realizar Cobro','accion':'Pagos Pendientes'})
            except Lectura.DoesNotExist:
                return render(request, 'buscarSocio.html',{'objetos':alllecturasSinpagar,'form':form, 'tipo':'Cobrar','subtipo':'Realizar Cobro','accion':'Buscar Socio'})
    return render(request, 'buscarSocio.html',{'objetos':alllecturasSinpagar,'form':form, 'tipo':'Cobrar','subtipo':'Realizar Cobro','accion':'Buscar Socio'})

class RealizarCobroViews(UpdateView):
    template_name = 'cobrarlectura.html'
    success_url = reverse_lazy('buscarSocioCobrar')

    def get(self, request, *args, **kwargs):
        lectura = get_object_or_404(Lectura,id=kwargs['pk'])
        lectura.fechapago = date.today()
        form = CobrarLecturaForm(instance=lectura)
        # form = CobrarLecturaForm(initial={
        #     'anterior':lectura.anterior,
        #     'actual':lectura.actual,
        #     'consumo':lectura.consumo,
        #     'pagoconsumo':lectura.pagoconsumo,
        #     'multa':lectura.multa,
        #     'pagototal':lectura.pagototal,
        #     'fecha':lectura.fecha,
        #     'mes':lectura.mes,
        #     'anio':lectura.anio,
        #     'estado':lectura.estado,
        #     'socio':lectura.socio,
        # })
        return render(request, self.template_name, { 'form':form,'tipo':'Cobrar','subtipo':'Realizar Cobro','accion':'Ver Recibo' })
    
    def post(self, request, *args, **kwargs):
        lectura = get_object_or_404(Lectura,id=kwargs['pk'])
        lectura.fechapago = date.today()
        lectura.estado=True
        lectura.save()
        cobrar = Cobrar()
        cobrar.fecha = date.today()
        cobrar.lectura = lectura
        cobrar.save()
        return render(request,self.success_url)