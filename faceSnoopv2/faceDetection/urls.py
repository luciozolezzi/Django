from django.urls import path

from . import views

app_name='faceDetection'
urlpatterns = [
    path('', views.index , name='index'),
    path('legajo/', views.legajo, name='legajo'),
    path('formulario/', views.formulario , name='formulario'),
    path('query/', views.query , name='query'),
]
