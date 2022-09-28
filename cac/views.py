from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola mundo Django')
    pass

def saludar(request,nombre):
    return HttpResponse(f"""
        <h1>Hola mundo Django - un gusto {nombre}</h1>    
    """)