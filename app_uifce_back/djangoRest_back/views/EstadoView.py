from djangoRest_back.serializers import EstadoSerializer
from djangoRest_back.models import Estado
from rest_framework import generics

""" Permisos para admin """

## Creacion de estados

class CrearEstado(generics.CreateAPIView):
    serializer_class = EstadoSerializer

## Ver, Actualizar y borrar estados

class RUDEstado(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()