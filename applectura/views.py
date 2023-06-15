from django.shortcuts import render, redirect
from applectura.forms import buscarSocioForm, realizarLecturaForm
from appsocio.models import Socio
from applectura.models import Lectura
from datetime import date
# Create your views here.

def buscarSocio(request):
    form = buscarSocioForm()
    allsocios = Socio.objects.all()

    if request.method == 'POST':
        form = buscarSocioForm(request.POST)
        if form.is_valid:
            id = request.POST['codigo']
            return redirect('realizarLectura', pk=id)
        else:
            print('invalido')
    return render(request, 'buscarSocio.html',{'socios':allsocios,'form':form})

def realizarLectura(request, pk):
    socio = Socio.objects.get(id=pk)
    anterior=lecturaAnterior(pk)
    fecha = date.today().strftime('%d-%m-%Y')
    mes = mesAnterior(date.today().month)
    anio = anioMes(date.today().month)
    form = realizarLecturaForm(initial={
        'anterior':anterior,
        'fecha':fecha,
        'mes':mes,
        'anio':anio,
        'socio':socio
    } )
    if ((request.method=='POST') and (anterior<=int(request.POST['actual']))):
        form =realizarLecturaForm(request.POST)
        if form.is_valid():
            lectura = Lectura()
            lectura.anterior=form.cleaned_data['anterior']
            lectura.actual=form.cleaned_data['actual']
            lectura.fecha=form.cleaned_data['fecha']
            lectura.mes=form.cleaned_data['mes']
            lectura.anio=form.cleaned_data['anio']
            lectura.socio=form.cleaned_data['socio']
    return render(request,'realizarLectura.html',{'form':form, 'socio':socio})

def validarLectura(request,lectura):
    return render(request,'.html',{'form':form})

def lecturaAnterior(pk):
    mesAnt=mesAnterior(date.today().month-1)
    anioAnt=anioMes(date.today().month-1)
    lectura = Lectura.objects.get(socio=pk,anio=anioAnt,mes=mesAnt)
    return lectura.actual

def mesAnterior(mes):
    mes = mes-1
    if mes==1:mes='ENERO'
    elif mes==2:mes='FEBRERO'
    elif mes==3:mes='MARZO'
    elif mes==4:mes='ABRIL'
    elif mes==5:mes='MAYO'
    elif mes==6:mes='JUNIO'
    elif mes==7:mes='JULIO'
    elif mes==8:mes='AGOSTO'
    elif mes==9:mes='SEPTIEMBRE'
    elif mes==10:mes='OCTUBRE'
    elif mes==11:mes='NOVIEMBRE'
    elif mes==0:mes='DICIEMBRE'
    else:mes='NOVIEMBRE'
    return mes

def anioMes(mes):
    mes-=1
    anio=date.today().year
    if mes<=0:anio-=1
    return anio
