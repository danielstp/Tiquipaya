from django.db import models
from datetime import datetime


class Sexo(models.Model):
    nombre = models.CharField(max_length=255, primary_key=True)
    orden = models.IntergerField()

    def __str__(self):
        return self.nombre


class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=255, primary_key=True)
    orden = models.IntergerField()

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellidoPaterno = models.CharField(max_length=255)
    apellidoMaterno = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()

    def edad(self):
        return datetime.now() - self.fechaNacimiento


