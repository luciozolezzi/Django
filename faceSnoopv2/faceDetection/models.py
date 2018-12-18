# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import json



# Create your models here.


class Empleado(models.Model):
    legajo=models.IntegerField()
    nombre=models.CharField(max_length=140)
    ingreso=models.TimeField('Horario de ingreso')  #'%H:%M:%S'
    egreso=models.TimeField('Horario de egreso')    #'%H:%M:%S'

    def __str__(self):
        return self.nombre

class FaceRectangle(models.Model):
    legajo=models.IntegerField()
    top=models.IntegerField()
    left=models.IntegerField()
    width=models.IntegerField()
    heigth=models.IntegerField()

    def __str__(self):
        return str(self.legajo)
