from django.urls import path
from .views import *

urlpatterns = [

    path('', inicio, name='inicio'),
    path('servicios/', servicios, name='servicios'),
    path('empleados/', empleados, name='empleados'),
    path('formPacientes', pacientes, name='formPacientes'),

]