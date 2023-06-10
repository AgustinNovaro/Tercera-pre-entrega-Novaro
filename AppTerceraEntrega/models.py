from django.db import models

# Create your models here.
class Receta(models.Model):
    titulo = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=200)
    tiempo_coccion = models.CharField(max_length=200)
    instrucciones = models.TextField()
    def __str__(self):
        return f"{self.titulo} - {self.sabor} - {self.tiempo_coccion} - {self.ingredientes} - {self.instrucciones}"

class Nutricion(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    matricula = models.CharField(max_length=20)
    especialidad = models.TextField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.matricula} - {self.especialidad}"

class Deportes(models.Model):
    deporte = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    deportista = models.CharField(max_length=100)
    atendido_por = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.deporte} - {self.pais} - {self.deportista} - {self.atendido_por}"
