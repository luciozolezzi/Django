# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Empleado,FaceRectangle

class EmpleadoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nombre del empleado', {'fields': ['nombre']}),
        ('Numero de legajo', {'fields': ['legajo']}),
        ('Horario de ingreso', {'fields': ['ingreso']}),
        ('Horario de egreso', {'fields': ['egreso']}),
    ]
    list_display=('nombre','legajo')        #Indica los campos que se muestran y el orden
    list_filter = ['nombre']                #Añade filtros para el campo nombre
    search_fields = ['nombre','legajo']     #Añade una caja de busqueda en admin
    list_per_page=20                        #Empleados mostrados por pagina


# Register your models here.

admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(FaceRectangle)
