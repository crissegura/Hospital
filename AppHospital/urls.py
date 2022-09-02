from django.urls import path
from .views import *

urlpatterns = [

    path('', inicio, name='inicio'),
    path('servicios/', servicios, name='servicios'),
    path('empleados/', empleados, name='empleados'),
    path('pacientes/', pacientes, name='pacientes'),
    path('buscarPaciente/', buscarPaciente, name='buscarPaciente'),
    path('buscar/', buscar, name='buscar'),

]