# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Empleado,FaceRectangle

# Register your models here.

admin.site.register(Empleado)
admin.site.register(FaceRectangle)
