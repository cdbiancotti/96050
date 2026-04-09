from django.db import models


class Sucursal(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    fecha_apertura = models.DateField()
    
    def __str__(self) -> str:
        return f"Sucursal: {self.nombre} - Apertura: {self.fecha_apertura}"