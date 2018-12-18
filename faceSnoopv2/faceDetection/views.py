# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Empleado

import json
import datetime

def index(request):
    try:
        top_5=Empleado.objects.order_by('legajo')[:5]
        context = {
            'top_5': top_5,
        }
    except Empleado.DoesNotExist:
        raise Http404("No existe el empleado que quiere buscar")
    return HttpResponse (render(request, 'faceDetection/index.html', context))

def legajo(request):
    output={}
    return HttpResponse(output)

def formulario(request):
    context={}
    return HttpResponse(render(request, 'faceDetection/formulario.html', context))

def query(request):
    #l=Empleado.objects
    e=Empleado(legajo=request.POST['legajo'],nombre=request.POST['nombre'],ingreso=request.POST['ingreso'],egreso=request.POST['egreso'])
    e.save()
    context={
        'legajo':request.POST['legajo'],
        'nombre':request.POST['nombre'],
        'ingreso':request.POST['ingreso'],
        'egreso':request.POST['egreso'],
    }
    return HttpResponse(render(request, 'faceDetection/query.html', context))
