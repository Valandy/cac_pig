from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse
from django.template import loader

# Create your views here.

def index(request):
    if(request.method=='GET'):
        titulo = 'Título cuando accedo por GET'
    else:
        titulo = f'Título cuando accedo por otr método {request.method}'
    parametros_get = request.GET.get('nombre')
    
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso_curso',
            'categoria':'Programación',
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion':'Curso_curso',
            'categoria':'Diseño',
        },
        {
            'nombre':'Big data',
            'descripcion':'test_test',
            'categoria':'Analisis de datos',
        },
    ]
    
    return render(request,'cac/index.html',{'titulo':titulo, 'cursos':listado_cursos})

def quienes_somos(request):
    template = loader.get_template('cac/quienes_somos.html')
    contexto = {'titulo':'Codo a Codo - Quienes somos',}
    return HttpResponse(template.render(contexto,request))


