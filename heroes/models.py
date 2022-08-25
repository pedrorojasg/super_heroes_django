from django.db import models

"""
Deberá tener un template, una vista y dos modelos (superHeroe y Poder)
La clase SuperHeroe, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas)

Se deberán crear como mínimo 3 superhéroes, cada uno con dos poderes
Los superheróes se deben ver desde la web
"""

class SuperHeroe(models.Model):
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    peso_kg = models.IntegerField()


class Poder(models.Model):
    nombre = models.CharField(max_length=128)
    super_heroe = models.ForeignKey('SuperHeroe', on_delete=models.CASCADE)
