from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    direccion = models.TextField(max_length=200, verbose_name="Direccion")
    ci = models.PositiveIntegerField(verbose_name="CI")
    telefono = models.PositiveIntegerField(verbose_name="Telefono")
