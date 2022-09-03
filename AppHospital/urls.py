from django.urls import path
from .views import *

urlpatterns = [

    path('', inicio, name='inicio'),
    path('servicios/', servicios, name='servicios'),
    path('empleados/', empleados, name='empleados'),
    path('pacientes/', pacientes, name='pacientes'),
    path('pacientes/', buscarPaciente, name='buscarPaciente'),
    path('buscar/', buscar, name='buscar'),
    path('empleados/',buscarEmpleado, name='buscarEmpleado'),
    path('buscarEmp/', buscarEmp , name='buscarEmp' ),
    path('servicios/', buscarServicio , name='buscarServicio' ),
    path('buscarServ/', buscarServ , name='buscarServ' ),
]