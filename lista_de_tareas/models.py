from django.db import models

# Create your models here.
from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True) 
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    hora = models.TimeField(null=True, blank=True)
    def __str__(self):
        return self.titulo
