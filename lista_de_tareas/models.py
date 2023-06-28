from django.db import models

# Create your models here.
from django.db import models

class Tarea(models.Model):
    DIAS_DE_LA_SEMANA = [
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
        (7, 'Domingo'),
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True) 
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    hora = models.TimeField(null=True, blank=True)
    dia = models.IntegerField(choices=DIAS_DE_LA_SEMANA)
    def __str__(self):
        return self.titulo
