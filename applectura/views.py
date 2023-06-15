from django.shortcuts import render, redirect
from applectura.forms import buscarSocioForm, realizarLecturaForm, lecturaForm
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
    if (request.method=='POST'): #Verificamos que el formulario haya sido enviado mediante mettdo POST
        if (anterior<=int(request.POST['actual'])): #Verificaomos que el valor de lectura anterior sea menor o igual a la lectura actual
            form =realizarLecturaForm(request.POST) #Cargamos todos los datos a form
            if form.is_valid(): #Verificamos que todos los campos tegan valores validos
                lectura = Lectura()
                lectura.anterior=form.cleaned_data['anterior']
                lectura.actual=form.cleaned_data['actual']
                lectura.consumo=lectura.actual-lectura.anterior
                lectura.pagoconsumo=calcularConsumo(lectura.actual,lectura.anterior)
                lectura.multa=calcularMulta()
                lectura.fecha=form.cleaned_data['fecha']
                lectura.mes=form.cleaned_data['mes']
                lectura.anio=form.cleaned_data['anio']
                lectura.estado=False
                lectura.socio=form.cleaned_data['socio']
                return render(request, 'imprimirLectura.html', {'lectura':lectura})
        else:
            alerta = 'btn-close'

    return render(request,'realizarLectura.html',{'form':form, 'socio':socio})

def validarLectura(request,pk):
    if request.method == 'POST':
        if int(request.POST['anterior'])<=int(request.POST['actual']):
            socio = Socio.objects.get(id=pk)
            form = lecturaForm(request.POST,initial={
                'socio':socio,
            })
            if form.is_valid():
                return render(request,'mipoup.html',{'form':form})

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
    lectura = Lectura.objects.get(anio=anioM,mes=mesM)
    if lectura.estado==False:
        multa=15
    return multa