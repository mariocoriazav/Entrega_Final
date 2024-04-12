from django.db import models

# Create your models here.

class Venta(models.Model):

    nombre_usuario = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return f"Este pedido está a nombre de {self.nombre_usuario} con el código de referencia {self.codigo}"