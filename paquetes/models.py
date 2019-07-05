from django.db import models

# Create your models here.
class Paquete(models.Model):
    destino = models.CharField(max_length=100, verbose_name="Destino")
    descripcion = models.TextField(verbose_name="Descripcion")
    precio = models.CharField(max_length=100, verbose_name="Precio")
    guia = models.CharField(max_length=100, verbose_name="Guia")
    fechaPartida = models.CharField(max_length=100, verbose_name="FechaPartida")

    def __str__(self):
        return self.name
