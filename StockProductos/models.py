from django.db import models
from django.contrib.auth.models import User

class Procesador(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    stock = models.IntegerField(default = 1)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    
    class Meta:
        ordering = ["precio"]
        verbose_name = "Procesador"
        verbose_name_plural = "Procesadores"
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.precio}, {self.descripcion}"
    
class PlacaVideo(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    stock = models.IntegerField(default = 1)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    
    class Meta:
        ordering = ["precio"]
        verbose_name = "Placa de video"
        verbose_name_plural = "Placas de video"
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.precio}, {self.descripcion}"
    
class Teclado(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    stock = models.IntegerField(default = 1)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    
    class Meta:
        ordering = ["precio"]
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.precio}, {self.descripcion}"
    
class Gabinete(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    stock = models.IntegerField(default = 1)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    
    class Meta:
        ordering = ["precio"]
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.precio}, {self.descripcion}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
