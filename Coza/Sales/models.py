from django.db import models

# Create your models here.

class Venta(models.Model):

    nombre_usuario = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return f"Este pedido está a nombre de {self.nombre_usuario} con el código de referencia {self.codigo}"


class Serie(models.Model):
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    capacidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}- Capacidad: {self.capacidad}"
    

class Inventario(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.producto}- Cantidad: {self.cantidad}"