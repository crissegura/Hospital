from dataclasses import fields
from socket import fromshare
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar email')
    password1= forms.CharField(label='Modificar contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir contraseña nueva', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar nombre')
    last_name=forms.CharField(label='Modificar apellido')

    class Meta:
        model=User
        fields=['email','password1','password2','first_name','last_name']
        help_texts = {k:"" for k in fields}

class FormPublicacion(forms.Form):
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)
    texto=forms.CharField(max_length=1000000000)
    autor=forms.CharField(max_length=50)
    imagen=forms.ImageField()


# class Nuevo_paciente(forms.Form):
#     nombre=forms.CharField(max_length=50)
#     edad=forms.IntegerField()
#     situacion=forms.CharField(max_length=200)
#     ultima_visita=forms.DateField()
#     fecha_regreso=forms.DateField()
#     email=forms.EmailField()

# class Nuevo_empleado(forms.Form):
#     nombre=forms.CharField(max_length=50)
#     edad=forms.IntegerField()
#     profesion=forms.CharField(max_length=50)
#     especializacion=forms.CharField(max_length=50)
#     sueldo=forms.IntegerField()
#     email=forms.EmailField()
#     fecha_inicio=forms.DateField()

# class Nuevo_servicio(forms.Form):
#     servicio=forms.CharField(max_length=50)
#     precio=forms.IntegerField()