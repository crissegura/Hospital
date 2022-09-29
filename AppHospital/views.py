from email.mime import image
from operator import le
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
                return render (request, 'AppHospital/inicio.html')
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
    return  render(request, 'AppHospital/registro.html', {'form':form, 'imagen':traerAvatar(request) } )

@login_required
def comentarios(request):
    if request.method=='POST':
        formulario=FormCom(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            comentario=info.get("comentario")
            user=request.user
            ncomentario=Comentario(comentario=comentario,comentarista=user)
            ncomentario.save()
            return render (request, 'AppHospital/comentarios.html',{'usuario':request.user})
    else:
        formulario=FormCom()
    return  render(request, 'AppHospital/comentarios.html', {'formulario':formulario, 'imagen':traerAvatar(request) } )
    


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
    return render (request, 'AppHospital/editarUser.html', {'form':form,'usuario':usuario, 'imagen':traerAvatar(request) })

@login_required
def traerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=''
    return imagen


def inicio (request):
    comentarios = Comentario.objects.all()
    return render (request,"AppHospital/inicio.html",{'imagen':traerAvatar(request),'comentarios': comentarios})

def sobreMi (request):
    return render (request, "AppHospital/sobreMi.html",{'imagen':traerAvatar(request)} )

@login_required
def publicaciones (request):
    if request.method == "POST":
        nuevaPublicacion=FormPublicacion(request.POST,request.FILES)
        print(nuevaPublicacion.is_valid())
        imagen=request.FILES['imagen']
        if nuevaPublicacion.is_valid():
            informacion=nuevaPublicacion.cleaned_data
            user=request.user
            titulo=informacion.get("titulo")
            subtitulo=informacion.get("subtitulo")
            texto=informacion.get("texto")
            imagen=informacion.get("imagen")
            publicacion=Publicacion(titulo=titulo,subtitulo=subtitulo,autor=user,
            texto=texto,imagen=imagen)
            publicacion.save()
            return render(request, "AppHospital/inicio.html",{'usuario':request.user} )
        else:
            print(nuevaPublicacion.errors)
            return render(request, "AppHospital/inicio.html")
    else:
        nuevaPublicacion=FormPublicacion()
        return render (request, "AppHospital/publicaciones.html",{'form':nuevaPublicacion, 'usuario':request.user ,'imagen':traerAvatar(request) } )

def leerPublicaciones (request):
    publicaciones = Publicacion.objects.all()
    texto='No hay publicaciones para ver.'
    if publicaciones:
        return render (request, 'AppHospital/leerPublicacion.html', {'publicaciones': publicaciones,'imagen':traerAvatar(request)})
    return render (request, 'AppHospital/leerPublicacion.html', {'texto':texto ,'imagen':traerAvatar(request)})


def leerComentarios (request):
    comentarios = Comentario.objects.all()
    texto='No hay comentarios aún.'
    if comentarios:
        return render (request, 'AppHospital/inicio.html', {'comentarios': comentarios})
    return render (request, 'AppHospital/inicio.html', {'texto':texto ,'imagen':traerAvatar(request)})


@login_required
def eliminarPublicacion (request, publicacion_publicacion):
    publicacion = Publicacion.objects.get(titulo=publicacion_publicacion)
    publicacion.delete()

    publicaciones = Publicacion.objects.all()
    context = {'publicaciones': publicaciones}

    return render( request, 'AppHospital/leerPublicacion.html', context )

@login_required
def editarPublicacion (request, publicacion_publicacion):
    publicacion = Publicacion.objects.get(titulo=publicacion_publicacion)
    if request.method =='POST':
        form=FormPublicacion(request.POST,request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            publicacion.titulo = info['titulo']
            publicacion.subtitulo = info['subtitulo']
            publicacion.texto = info['texto']
            if info['imagen']:
                publicacion.imagen = info['imagen']
            publicacion.save()
            publicaciones=Publicacion.objects.all()
            return render (request,"AppHospital/leerPublicacion.html",{'publicaciones':publicaciones})
    else: 
        form=FormPublicacion(initial={'titulo': publicacion.titulo,
        'subtitulo':publicacion.subtitulo,'texto':publicacion.texto,'imagen':publicacion.imagen})  
    return render(request, "AppHospital/editarPublicacion.html",
    {'form':form,'publicacion_publicacion':publicacion_publicacion})

@login_required
def agregarAvatar(request):
    if request.method=='POST':
        formulario = AvatarForm(request.POST,request.FILES) 
        if formulario.is_valid():
            avatarViejo = Avatar.objects.get(user=request.user)
            if (avatarViejo.imagen):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render (request, 'AppHospital/inicio.html',{'usuario':request.user})
    else:
        formulario=AvatarForm()
    return render (request, 'AppHospital/agregarAvatar.html',{'formulario':formulario,'usuario':request.user} )









