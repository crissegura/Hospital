from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.template import Context, Template,loader
from AppHospital.forms import *


def inicio (request):
    return render (request,"AppHospital/inicio.html")

def empleados (request):
    if request.method == "POST":
        nuevoEmpleado=Nuevo_empleado(request.POST)
        print(nuevoEmpleado)
        if nuevoEmpleado.is_valid():
            informacion=nuevoEmpleado.cleaned_data
            nombre=informacion.get("nombre")
            edad=informacion.get("edad")
            profesion=informacion.get("profesion")
            especializacion=informacion.get("especializacion")
            sueldo=informacion.get("sueldo")
            email=informacion.get("email")
            fecha_inicio=informacion.get("fecha_inicio")
            empleado=Empleados(nombre=nombre,edad=edad,profesion=profesion,especializacion=especializacion,
            sueldo=sueldo,email=email,fecha_inicio=fecha_inicio)
            empleado.save()
            return render(request, "AppHospital/inicio.html" )
        else:
            return render(request, "AppHospital/inicio.html")
    else:
        nuevoEmpleado=Nuevo_empleado()
        return render (request, "AppHospital/empleados.html", {"formulario":nuevoEmpleado})

def servicios (request):
    if request.method == "POST":
        nuevoServicio=Nuevo_servicio(request.POST)
        if nuevoServicio.is_valid():
            informacion=nuevoServicio.cleaned_data
            getServicio=informacion.get("servicio")
            getPrecio=informacion.get("precio")
            servicioAgregado=Servicios(servicio=getServicio,precio=getPrecio)
            servicioAgregado.save()
            return render(request, "AppHospital/inicio.html" )
        else:
            return render(request, "AppHospital/inicio.html")
    else:
        nuevoServicio=Nuevo_servicio()
        return render (request, "AppHospital/servicios.html", {"formulario":nuevoServicio})
   

    
def pacientes(request):
    if request.method == "POST":
        nuevoPaciente=Nuevo_paciente(request.POST)
        print(nuevoPaciente)
        if nuevoPaciente.is_valid():
            informacion=nuevoPaciente.cleaned_data
            nombre=informacion.get("nombre")
            edad=informacion.get("edad")
            situacion=informacion.get("situacion")
            ultima_visita=informacion.get("ultima_visita")
            fecha_regreso=informacion.get("fecha_regreso")
            email=informacion.get("email")
            paciente=Pacientes(nombre=nombre,edad=edad,situacion=situacion,
            ultima_visita=ultima_visita,fecha_regreso=fecha_regreso,email=email)
            paciente.save()
            return render(request, "AppHospital/inicio.html")
        else:
            return render(request, "AppHospital/inicio.html")
    else:
        nuevoPaciente=Nuevo_paciente()
        return render (request, "AppHospital/pacientes.html", {"formulario":nuevoPaciente})
    
    
def buscarPaciente(request):
    return render(request, "AppHospital/buscarPaciente.html")

def buscar(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        paciente=Pacientes.objects.filter(nombre__icontains=nombre)
        return render(request, "AppHospital/resultadosBusquedas.html", {"paciente":paciente, "nombre":nombre} )
    else:
        respuesta= 'No ingresaste ningun dato'

    return HttpResponse(respuesta) 




