# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Empleado,FaceRectangle

class EmpleadoAdmin(admin.ModelAdmin):
    fields=['nombre','legajo','ingreso','egreso']




# Register your models here.

admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(FaceRectangle)
