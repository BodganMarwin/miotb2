from django.shortcuts import render, redirect
from applectura.forms import buscarSocioForm
from appsocio.models import Socio

# Create your views here.

def buscarSocio(request):
    form = buscarSocioForm()
    allsocios = Socio.objects.all()

    if request.method == 'POST':
        # print(request.POST['codigo'])
        form = buscarSocioForm(request.POST)
        if form.is_valid:
            # print('valido')
            id = request.POST['codigo']
            socio = buscarSocioDB(id)
            print(socio.codigo)
        else:
            print('invalido')    
    return render(request, 'buscarSocio.html',{'socios':allsocios,'form':form})

def buscarSocioDB(id):
    return Socio.objects.get(id=id)

def realizarLectura(request, socio):
    return render(request,'realizarLectura.html',{'socio':socio})