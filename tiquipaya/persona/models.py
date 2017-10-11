from django.db import models
from datetime import datetime


class Sexo(models.Model):
    nombre = models.CharField(max_length=255, primary_key=True)
    orden = models.IntegerField()

    def __str__(self):
        return self.nombre


class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=255, primary_key=True)
    orden = models.IntegerField()

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellidoPaterno = models.CharField(max_length=255)
    apellidoMaterno = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    sexo = models.ForeignKey(Sexo, default="Femenino", on_delete=models.PROTECT)
    estadoCivil = models.ForeignKey(EstadoCivil, default='Soltero', on_delete=models.PROTECT)


    def edad(self):
        return datetime.date(datetime.today()) - self.fechaNacimiento


