"""
URL configuration for miotb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from applectura import views
from apptroncal.views import crearCliente,crearServicio,crearGeo
from appsocio.views import *
from applectura.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('buscarSocio/',views.buscarSocio, name='buscarSocio'),
    path('realizarLectura/<int:pk>/',views.realizarLectura, name='realizarLectura'),
    path('validarLectura/<int:pk>/',views.validarLectura, name='validarLectura'),
    # path('imprimirLectura/<int:pk>/',views.imprimirLectura, name='imprimirLectura'),
    # path('crearGeo/', crearGeo, name='crearGeo'),
    # path('crearCliente/', crearCliente, name='crearCliente'),
    # path('crearServicio/', crearServicio, name='crearServicio'),
    path('socio/listarsocio/', login_required(ListarSociosView.as_view()) , name='listarsocios'),
    path('socio/crearsocio/', login_required(CrearSocioView.as_view()) , name='crearsocio'),
    path('socio/editarsocio/<int:pk>/', login_required(EditarSocioView.as_view()) , name='editarsocio'),
    path('lectura/lectura/<int:pk>', login_required(PrimeraLecturaView.as_view()) , name='primeralectura'),
    path('lectura/impimir/<int:pk>/', login_required(views.imprimirLectura) , name='imprimirLectura'),
]
