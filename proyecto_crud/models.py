from django.db import models

# Create your models here.
class proyectocrud(models.Model):
    fecha_ent = models.DateTimeField()
    observaciones = models.TextField()
    fecha_sal = models.DateTimeField()
    creado = models.DateTimeField(auto_now_add=True)