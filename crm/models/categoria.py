from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"NombreCategoria: {self.name}, TagsCategoria: {self.tag},"
