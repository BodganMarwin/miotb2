from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from applectura.forms import *
from appsocio.models import Socio
from applectura.models import Lectura
from datetime import date
from .views import *
# Create your views here.

def buscarSocio(request):
    form = buscarSocioForm()
    
    allsocios = Socio.objects.all()
    mes = mesAnterior(date.today().month)
    anio = anioMes(date.today().month)
    alllecturasmes = Lectura.objects.filter(anterior__gt=0,mes=mes,anio=anio)
    if request.method == 'POST':
        form = buscarSocioForm(request.POST)
        if form.is_valid:
            id = request.POST['codigo']
            socio = Socio.objects.get(id=id)
            try:
                Lectura.objects.get(socio=socio,anio=anio,mes=mes)
                return render(request, 'buscarSocio.html',{'objetos':alllecturasmes,'form':form, 'tipo':'Lectura','subtipo':'Realizar Lectura','accion':'Buscar Socio'})
            except Lectura.DoesNotExist:
                return redirect('realizarLectura', pk=id)
    return render(request, 'buscarSocio.html',{'objetos':alllecturasmes,'form':form,'tipo':'Lectura','subtipo':'Realizar Lectura','accion':'Buscar Socio'})

class PrimeraLecturaView(CreateView):
    model = Lectura
    # form_class = PrimeraLecturaForm(initial={'fecha':date.today().strftime('%d-%m-%Y')})
    form_class = PrimeraLecturaForm
    template_name = 'lectura/primeralectura.html'
    success_url = reverse_lazy('buscarSocio')

    def get(self, request, *args, **kwargs):
        socio = Socio.objects.get(id=kwargs['pk'])
        mes = mesAnterior(date.today().month)
        return render(request,self.template_name,{'form':self.form_class,'socio':socio, 'mes':mes})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        socio = Socio.objects.get(id=kwargs['pk'])
        mes = mesAnterior(date.today().month)
        if form.is_valid():
            lectura = Lectura(
                anterior = 0,
                actual= form.cleaned_data['actual'],
                consumo = 0,
                pagoconsumo = 0,
                multa = 0,
                pagototal = 0,
                fechaemision = date.today(),
                mes = mes,
                anio = anioMes(date.today().month-1),
                estado = False,
                socio = socio,
            )
            
            print(lectura)
            lectura.save()
            return redirect(self.success_url)
        return render(request,self.template_name,{'form':self.form_class,'socio':socio, 'mes':mes})

def realizarLectura(request, pk):
    socio = Socio.objects.get(id=pk)
    if Lectura.objects.filter(socio=pk):
        ultima = ultimaLectura(pk,date.today().year)
        # lecturas = Lectura.objects.get(socio=pk,anio=2023,mes='JUNIO')
        # lecturas = Lectura.objects.filter(socio=pk)
        # for lectura in lecturas:
        #     print(lectura)
        # if existenlecturas:
        #     ultimomes = existenlecturas.mes
        #     ultimoanio = existenlecturas.anio

        # anterior=ultima.actual
        fecha = date.today().strftime('%d-%m-%Y')
        # mes = mesAnterior(date.today().month)
        # mes = getMes(ultima.mes)
        mes = mesAnterior(getMes(ultima.mes)+2)
        if ultima.mes == 'DICIEMBRE':
            anio = int(ultima.anio)+1
        else:
            anio = ultima.anio
        # anio = anioMes(getMes(ultima.mes))
        form = realizarLecturaForm(initial={
            'anterior':ultima.actual,
            'fechaemision':fecha,
            'mes':mes,
            'anio':anio,
            'multa':calcularMulta(),
            'socio':socio,
        } )
        if (request.method=='POST'): #Verificamos que el formulario haya sido enviado mediante mettdo POST
            if (ultima.actual<=int(request.POST['actual'])): #Verificaomos que el valor de lectura anterior sea menor o igual a la lectura actual
                form =realizarLecturaForm(request.POST) #Cargamos todos los datos a form
                if form.is_valid: #Verificamos que todos los campos tegan valores validos
                    print('es valido')
                    lectura = Lectura()
                    lectura.anterior=ultima.actual
                    lectura.actual=request.POST['actual']
                    lectura.consumo=float(request.POST['actual'])-ultima.actual
                    lectura.pagoconsumo=calcularConsumo(float(lectura.actual),float(lectura.anterior))
                    lectura.multa=calcularMulta()
                    lectura.pagototal=lectura.pagoconsumo+lectura.multa
                    lectura.fechaemision=date.today()
                    lectura.mes=mes
                    lectura.anio=anio
                    lectura.estado=False
                    lectura.socio=socio
                    try:
                        Lectura.objects.get(socio=lectura.socio,anio=lectura.anio,mes=lectura.mes)
                        return redirect('buscarSocio')
                    except Lectura.DoesNotExist:
                        lectura.save()
                        return redirect('imprimirLectura',pk=lectura.id)
        return render(request,'realizarLectura.html',{'form':form, 'socio':socio})
    else:
        return redirect('primeralectura',pk=pk)

def validarLectura(request,pk):
    if request.method == 'POST':
        if int(request.POST['anterior'])<=int(request.POST['actual']):
            socio = Socio.objects.get(id=pk)
            form = LecturaForm(request.POST,initial={
                'socio':socio,
            })
            if form.is_valid():
                return render(request,'mipoup.html',{'form':form})

def imprimirLectura(request,pk):
    lectura = Lectura.objects.get(id=pk)
    socio = Socio.objects.get(id=lectura.socio.id)
    return render(request, 'imprimirLectura.html',{'lectura':lectura,'socio':socio})

def lecturaAnterior(pk):
    mesAnt=mesAnterior(date.today().month-1)
    anioAnt=anioMes(date.today().month-1)
    lectura = Lectura.objects.get(socio=pk,anio=anioAnt,mes=mesAnt)
    return lectura.actual

def ultimaLectura(pk,anio):
    try: 
        Lectura.objects.filter(socio=pk)
        lecturas = Lectura.objects.filter(socio=pk,anio=anio)
        if lecturas:
            return lecturas.last()
        else:
            return ultimaLectura(pk,anio-1)
    except Lectura.DoesNotExist:
        return None

def mesAnterior(mes):
    mes = mes-1
    if mes==2:mes='FEBRERO'
    elif mes==3:mes='MARZO'
    elif mes==4:mes='ABRIL'
    elif mes==5:mes='MAYO'
    elif mes==6:mes='JUNIO'
    elif mes==7:mes='JULIO'
    elif mes==8:mes='AGOSTO'
    elif mes==9:mes='SEPTIEMBRE'
    elif mes==10:mes='OCTUBRE'
    elif mes==11:mes='NOVIEMBRE'
    elif mes==12:mes='DICIEMBRE'
    else: mes='ENERO'
    return mes

def anioMes(mes):
    mes-=1
    anio=date.today().year
    if mes<=0:anio-=1
    return anio
def calcularConsumo(actual, anterior):
    consumo = actual - anterior
    monto = 15
    if consumo>15 and consumo<=20:
        res = consumo - 15
        monto = monto + 3*res
    elif consumo>20:
        res = consumo - 20
        monto = 30 + res*5 
    return monto
def calcularMulta():
    multa=0
    mesM=mesAnterior(date.today().month-2)

    anioM=anioMes(date.today().month-2)
    try:
        lectura = Lectura.objects.get(anio=anioM,mes=mesM)
    except Lectura.DoesNotExist:
        lectura = None
    if lectura:
        if lectura.estado==False:
            multa=15
    return multa

def getMes(mes):
    if mes=='ENERO':mes=1
    elif mes=='FEBRERO':mes=2
    elif mes=='MARZO':mes=3
    elif mes=='ABRIL':mes=4
    elif mes=='MAYO':mes=5
    elif mes=='JUNIO':mes=6
    elif mes=='JULIO':mes=7
    elif mes=='AGOSTO':mes=8
    elif mes=='SEPTIEMBRE':mes=9
    elif mes=='OCTUBRE':mes=10
    elif mes=='NOVIEMBRE':mes=11
    elif mes=='DICIEMBRE':mes=12
    return mes
