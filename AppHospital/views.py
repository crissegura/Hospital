from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.template import Context, Template,loader
from AppHospital.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            usuario = authenticate(username=user,password=password)
            if usuario is not None:
                login(request, usuario)
                return render (request, 'AppHospital/inicio.html', {'mensaje':f'Bienvenido {user}. '} )
            else:
                return render(request, 'AppHospital/login.html', {'mensaje':f'No se pudo iniciar sesión. Datos incorrectos.','form':form} )
        else:
            return  render(request, 'AppHospital/login.html', {'mensaje':f'Error, formulario erróneo.', 'form':form} )
    form=AuthenticationForm()
    return  render(request, 'AppHospital/login.html', {'form':form} )

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render (request, 'AppHospital/inicio.html', {'mensaje':'Usuario creado exitosamente!'} )
    else:
        form = UserRegisterForm()
    return  render(request, 'AppHospital/registro.html', {'form':form} )

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method=='POST':
        form=UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.save()
            return render (request, 'AppHospital/inicio.html', {'mensaje':f'Usuario editado'})
    else:
        form=UserEditForm(request.POST)
    return render (request, 'AppHospital/editarUser.html', {'form':form,'usuario':usuario})


def inicio (request):
    return render (request,"AppHospital/inicio.html")

def sobreMi (request):
    return render (request, "AppHospital/sobreMi.html" )

@login_required
def publicaciones (request):
    if request.method == "POST":
        nuevaPublicacion=FormPublicacion(request.POST,request.FILES)
        print(nuevaPublicacion.is_valid())
        imagen=request.FILES['imagen']
        if nuevaPublicacion.is_valid():
            informacion=nuevaPublicacion.cleaned_data
            titulo=informacion.get("titulo")
            subtitulo=informacion.get("subtitulo")
            texto=informacion.get("texto")
            autor=informacion.get("autor")
            imagen=informacion.get("imagen")
            publicacion=Publicacion(titulo=titulo,subtitulo=subtitulo,
            texto=texto,autor=autor,imagen=imagen,)
            publicacion.save()
            return render(request, "AppHospital/inicio.html" )
        else:
            print(nuevaPublicacion.errors)
            return render(request, "AppHospital/inicio.html")
    else:
        nuevaPublicacion=FormPublicacion()
        return render (request, "AppHospital/publicaciones.html",{'form':nuevaPublicacion} )

def leerPublicaciones (request):
    publicaciones = Publicacion.objects.all()
    context = {'publicaciones': publicaciones}
    return render (request, 'AppHospital/leerPublicacion.html', context)



# @login_required
# def leerEmpleados (request):
#     empleados = Empleados.objects.all()
#     context = {'empleados': empleados}
#     return render (request, 'AppHospital/leeremp.html', context)

# def eliminarEmpleado (request, empleado_nombre):
#     empleado = Empleados.objects.get(nombre=empleado_nombre)
#     empleado.delete()

#     empleados = Empleados.objects.all()
#     context = {'empleados': empleados}

#     return render( request, 'AppHospital/leeremp.html', context )

# def editarEmpleado (request, empleado_nombre):
#     empleado = Empleados.objects.get(nombre=empleado_nombre)
#     if request.method =='POST':
#         form=Nuevo_empleado(request.POST)
#         print(form)
#         if form.is_valid:
#             info=form.cleaned_data
#             empleado.nombre = info['nombre']
#             empleado.edad = info['edad']
#             empleado.profesion = info['profesion']
#             empleado.especializacion = info['especializacion']
#             empleado.sueldo = info['sueldo']
#             empleado.email = info['email']
#             empleado.fecha_inicio= info['fecha_inicio']
#             empleado.save()
#             empleados=Empleados.objects.all()
#             return render (request,"AppHospital/leeremp.html",{'empleados':empleados})
#     else: 
#         form=Nuevo_empleado(initial={'nombre':empleado.nombre,
#         'edad':empleado.edad,'profesion':empleado.profesion,
#         'especializacion':empleado.especializacion,
#         'sueldo':empleado.sueldo, 'email': empleado.email,'fecha_inicio':empleado.fecha_inicio })  
#     return render(request, "AppHospital/editarEmpleado.html",
#     {'form':form,'empleado_nombre':empleado_nombre})    

# def empleados (request):
#     if request.method == "POST":
#         nuevoEmpleado=Nuevo_empleado(request.POST)
#         print(nuevoEmpleado)
#         if nuevoEmpleado.is_valid():
#             informacion=nuevoEmpleado.cleaned_data
#             nombre=informacion.get("nombre")
#             edad=informacion.get("edad")
#             profesion=informacion.get("profesion")
#             especializacion=informacion.get("especializacion")
#             sueldo=informacion.get("sueldo")
#             email=informacion.get("email")
#             fecha_inicio=informacion.get("fecha_inicio")
#             empleado=Empleados(nombre=nombre,edad=edad,profesion=profesion,especializacion=especializacion,
#             sueldo=sueldo,email=email,fecha_inicio=fecha_inicio)
#             empleado.save()
#             return render(request, "AppHospital/inicio.html" )
#         else:
#             return render(request, "AppHospital/inicio.html")
#     else:
#         nuevoEmpleado=Nuevo_empleado()
#         return render (request, "AppHospital/empleados.html", {"formulario":nuevoEmpleado})

# def servicios (request):
#     if request.method == "POST":
#         nuevoServicio=Nuevo_servicio(request.POST)
#         if nuevoServicio.is_valid():
#             informacion=nuevoServicio.cleaned_data
#             getServicio=informacion.get("servicio")
#             getPrecio=informacion.get("precio")
#             servicioAgregado=Servicios(servicio=getServicio,precio=getPrecio)
#             servicioAgregado.save()
#             return render(request, "AppHospital/inicio.html" )
#         else:
#             return render(request, "AppHospital/inicio.html")
#     else:
#         nuevoServicio=Nuevo_servicio()
#         return render (request, "AppHospital/servicios.html", {"formulario":nuevoServicio})
   

    
# def pacientes(request):
#     if request.method == "POST":
#         nuevoPaciente=Nuevo_paciente(request.POST)
#         print(nuevoPaciente)
#         if nuevoPaciente.is_valid():
#             informacion=nuevoPaciente.cleaned_data
#             nombre=informacion.get("nombre")
#             edad=informacion.get("edad")
#             situacion=informacion.get("situacion")
#             ultima_visita=informacion.get("ultima_visita")
#             fecha_regreso=informacion.get("fecha_regreso")
#             email=informacion.get("email")
#             paciente=Pacientes(nombre=nombre,edad=edad,situacion=situacion,
#             ultima_visita=ultima_visita,fecha_regreso=fecha_regreso,email=email)
#             paciente.save()
#             return render(request, "AppHospital/inicio.html")
#         else:
#             return render(request, "AppHospital/inicio.html")
#     else:
#         nuevoPaciente=Nuevo_paciente()
#         return render (request, "AppHospital/pacientes.html", {"formulario":nuevoPaciente})
    
    
# def buscarPaciente(request):
#     return render(request, "AppHospital/pacientes.html")

# def buscar(request):
#     nombre=request.GET['nombre']
#     paciente=Pacientes.objects.filter(nombre=nombre)
#     if len(paciente)!=0:
#         return render(request, "AppHospital/resultadosBusquedas.html", {"paciente":paciente, "nombre":nombre} )
#     else:
#         return render(request, "AppHospital/resultadosBusquedas.html", {"mensaje":'Paciente no registrado'} )
    
# def buscarEmpleado(request):
#     return render (request, "AppHospital/empleados.html")

# def buscarEmp(request):
#     nombre=request.GET['nombre']
#     empleados=Empleados.objects.filter(nombre=nombre)
#     if len(empleados)!=0:
#         return render(request, "AppHospital/resultadosBusquedas.html", {"empleados":empleados, "nombre":nombre} )
#     else:
#         return render(request, "AppHospital/resultadosBusquedas.html", {"mensaje":'Esta persona no trabaja aquí.'} )

# def buscarServicio(request):
#     return render (request, "AppHospital/servicios.html")

# def buscarServ(request):
#     servicio=request.GET['nombre']
#     miServicio=Servicios.objects.filter(servicio=servicio)
#     if len(miServicio)!=0:
#         return render(request, "AppHospital/resultadosBusquedas.html", {"miServicio":miServicio, "servicio":servicio} )
#     else:
#         return render(request, "AppHospital/resultadosBusquedas.html", {"mensaje":'No realizamos este servicio en el Hospital.'} )


    





