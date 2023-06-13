from django.shortcuts import render
from applectura.forms import buscarSocioForm
from appsocio.models import Socio

# Create your views here.

def buscarSocio(request):
    form = buscarSocioForm()
    allsocios = Socio.objects.all()

    if request.method == 'POST':
        socio = request.codigo
        return render(request,'realizarLectura.html',{'socio':socio})

    return render(request, 'buscarSocio.html',{'socios':allsocios,'form':form})