from django.db import models
from .categoria import Categoria


class Producto(models.Model):
    name = models.CharField(max_length=255)
    descrip = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"NombreProducto: {self.name}, DescripProducto: {self.descrip},"
