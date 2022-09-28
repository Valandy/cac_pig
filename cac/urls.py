from django.urls import path, re_path
from . import views


urlpatterns = [
    path('',views.index, name='inicio'),
    path('hola_mundo', views.hola_mundo),
    
    #saludos
    path('saludar/',views.saludar, name='saludar_solito'),
    path('saludar/<str:nombre>', views.saludar, name='saludar'),
    
    
    #about
    path('quienessomos/',views.quienes_somos, name='quienes_somos'),
    
    #proyectos
    path('proyectos/<int:anio>/<int:mes>',views.ver_proyectos,name="ver_proyectos"),
    re_path(r'^proyectos/(?P<anio>\d{4})/$',views.ver_proyectos,name="ver_proyectos_anio"),
    
    #cursos
    path('cursos/detalle/<slug:nombre_curso>/',views.cursos_detalle,name='cursos_detalle'),
    re_path(r'^cursos/(?P<nombre_categoria>\w+)/$',views.cursos,name='cursos'),
]