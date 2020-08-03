from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=40,null=True)

    def __str__(self):
        return "%s / %s" %(self.nombre,self.password)


class Tarea(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=300)
    prioridad = models.CharField(max_length=20)
    creador = models.CharField(max_length=20,null=True)

    def __str__(self):
        return "%s/%s/%s" %(self.nombre,self.descripcion,self.prioridad)