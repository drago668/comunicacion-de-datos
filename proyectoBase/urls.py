"""
URL configuration for proyectoBase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from comunicacion.views import fm,mensaje, calcular,home,prueba,am,fsk,ask,decibeles,calcular1,lab

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('mensaje/',mensaje,name='mensaje'),
    path('fm/', fm, name='fm'),
    path('calculadora/', calcular, name='calculadora'),
    path('calculadora/', calcular, name='calculadora'),
    path('prueba/',prueba,name='prueba'),
    path('am/',am,name='am'),
    path('fsk/',fsk,name='fsk'),
    path('ask/',ask,name='ask'),
    path('decibeles/',decibeles,name='decibeles'),
    path('radioenlace/', calcular1, name='radioenlace_calcular'),
    path('labview/', lab, name='lab'),
]
