from django.db import models


class Pacientes(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    situacion=models.CharField(max_length=200)
    ultima_visita=models.DateField()
    fecha_regreso=models.DateField()
    email=models.EmailField()
    def __str__(self) -> str:
        return self.nombre
    


class Empleados(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=50)
    especializacion=models.CharField(max_length=50)
    sueldo=models.IntegerField()
    email=models.EmailField()
    fecha_inicio=models.DateField()
    def __str__(self) -> str:
        return self.nombre
    
class Servicios(models.Model):
    servicio=models.CharField(max_length=50)
    precio=models.IntegerField()
    def __str__(self) -> str:
        return self.servicio
    





    
    