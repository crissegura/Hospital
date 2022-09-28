from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Publicacion(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    texto=models.CharField(max_length=1000000000)
    autor=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='photos',null=True, blank=True)
    fecha= models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.titulo




class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars',null=True, blank=True)

    
    