from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self) -> str:
        return f'Prodcuto: {self.nombre}'