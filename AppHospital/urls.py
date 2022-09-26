from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', login_request, name='login'),
    path('register', register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppHospital/logout.html'), name='logout'),
    path('', inicio, name='inicio'),
    path('sobreMi/', sobreMi ,name='sobreMi'),
    path('servicios/', servicios, name='servicios'),
    path('empleados/', empleados, name='empleados'),
    path('pacientes/', pacientes, name='pacientes'),
    path('pacientes/', buscarPaciente, name='buscarPaciente'),
    path('buscar/', buscar, name='buscar'),
    path('empleados/',buscarEmpleado, name='buscarEmpleado'),
    path('buscarEmp/', buscarEmp , name='buscarEmp' ),
    path('servicios/', buscarServicio , name='buscarServicio' ),
    path('buscarServ/', buscarServ , name='buscarServ' ),
    path('leerEmpleados/', leerEmpleados , name='leerEmpleados' ),
    path('eliminarEmpleado/<empleado_nombre>/', eliminarEmpleado , name='eliminarEmpleado' ),
    path('editarEmpleado/<empleado_nombre>/', editarEmpleado , name='editarEmpleado' ),
]