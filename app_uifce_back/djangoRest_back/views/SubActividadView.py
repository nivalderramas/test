from ast import Sub
from djangoRest_back.serializers import SubActividadSerializer
from djangoRest_back.models import SubActividad
from rest_framework import generics

""" Permisos para todo tipo de Usuario """

## Lista de todas las subactividades

class ListarSubActividades(generics.ListAPIView):
    queryset = SubActividad.objects.all()

""" Permisos para todo usuario menos jefe """

## Actualizar las subactividades 

class ActualizarSubActividades(generics.UpdateAPIView):
    queryset = SubActividad.objects.all()
    serializer_class = SubActividadSerializer


""" Permisos para Master, Coordi y admin """

## Creacion de subactividades

class CrearSubActividades(generics.CreateAPIView):
    serializer_class = SubActividadSerializer

## Borrar subactividades

class BorrarSubActividades(generics.DestroyAPIView):
    serializer_class = SubActividadSerializer
    queryset = SubActividad.objects.all()