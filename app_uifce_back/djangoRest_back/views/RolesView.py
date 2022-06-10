from djangoRest_back.serializers import RolSerializer
from djangoRest_back.models import Rol 
from rest_framework import generics


""" Permisos para admin """

## Creacion de roles

class CrearRol(generics.CreateAPIView):
    serializer_class = RolSerializer

## Ver, Actualizar y borrar roles

class RUDRol(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()