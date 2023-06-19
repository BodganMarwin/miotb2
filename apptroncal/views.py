from django.shortcuts import render, redirect
from apptroncal.forms import GeoForm, ClienteForm, ServicioForm
from apptroncal.models import Servicio, Cliente, Georeferencias

# Create your views here.

def crearGeo(request):
    form = GeoForm()
    if request.method == 'POST':
        form = GeoForm(request.POST)
        if form.is_valid():
            geo = Georeferencias()
            geo.punto = request.POST['punto']
            geo.linea = request.POST['linea']
            geo.poligono = request.POST['poligono']
            geo.multipunto = request.POST['multipunto']
            geo.multilinea = request.POST['multilinea']
            geo.multipoligono = request.POST['multipoligono']
            geo.save()
            return redirect('crearGeo')
    return render(request, 'crearGeo.html', {'form':form})

def crearCliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente()
            cliente.nombre = request.POST['nombre']
            cliente.apellido = request.POST['apellido']
            cliente.genero = request.POST['genero']
            cliente.medalla = request.POST['medalla']
            cliente.ci = request.POST['ci']
            cliente.servicio = request.POST['servicio']
            cliente.save()
            return redirect('crearCliente')
    return render(request, 'crearCliente.html', {'form':form})


def crearServicio(request):
    form = ServicioForm()
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            servicio = Servicio()
            servicio.nombre = request.POST['nombre']
            servicio.save()
            return redirect('crearServicio')
    return render(request, 'crearServicio.html', {'form':form})
