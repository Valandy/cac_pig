from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse


# Create your views here.

def index(request):
    if(request.method=='GET'):
        titulo = 'Título cuando accedo por GET'
    else:
        titulo = f'Título cuando accedo por otr método {request.method}'
    parametros_get = request.GET.get('nombre')
    return HttpResponse(f"""
        <h1>{titulo}</h1>
        <p>{parametros_get}</p>
        """)

def hola_mundo(request):
    return HttpResponse('Hola mundo Django')
    pass

def saludar(request,nombre='Valentín'):
    return HttpResponse(f"""
        <h1>Hola mundo Django - un gusto {nombre}</h1>    
    """)
    
def ver_proyectos(request,anio,mes=1):
    return HttpResponse(f"""
        <h1>Proyectos del {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
        """)
    
def cursos_detalle(request, nombre_curso):
    return HttpResponse(f'{nombre_curso}')

    
def cursos(request, nombre_categoria):
    return HttpResponse(f'{nombre_categoria}')

def quienes_somos(request):
    return redirect(reverse('saludar', kwargs={'nombre' : 'Roberto'}))
#   return redirect('saludar_solito')
