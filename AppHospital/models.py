from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo=models.CharField(max_length=20)
    subtitulo=models.CharField(max_length=20)
    texto=models.CharField(max_length=1000000000)
    autor=models.CharField(max_length=10)
    imagen=models.ImageField(upload_to='photos')
    fecha= models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.titulo




# class Avatar(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     imagen = models.ImageField(upload_to='avatars', null=True, blank=True)

# class Pacientes(models.Model):
#     nombre=models.CharField(max_length=50)
#     edad=models.IntegerField()
#     situacion=models.CharField(max_length=200)
#     ultima_visita=models.DateField()
#     fecha_regreso=models.DateField()
#     email=models.EmailField()
#     def __str__(self) -> str:
#         return self.nombre
    


# class Empleados(models.Model):
#     nombre=models.CharField(max_length=50)
#     edad=models.IntegerField()
#     profesion=models.CharField(max_length=50)
#     especializacion=models.CharField(max_length=50)
#     sueldo=models.IntegerField()
#     email=models.EmailField()
#     fecha_inicio=models.DateField()
#     def __str__(self) -> str:
#         return self.nombre
    
# class Servicios(models.Model):
#     servicio=models.CharField(max_length=50)
#     precio=models.IntegerField()
#     def __str__(self) -> str:
#         return self.servicio
    





    
    