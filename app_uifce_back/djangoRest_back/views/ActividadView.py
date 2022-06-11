from djangoRest_back.serializers import ActividadSerializer
from djangoRest_back.models import Actividad
from rest_framework import generics

""" Permisos para todo tipo de Usuario """


## Lista de las actividades

class ListarActividades(generics.ListAPIView):
    queryset = Actividad.objects.all()


""" Permisos para Master, Coordi y admin """


## Creacion de actividades

class CrearActividades(generics.CreateAPIView):
    serializer_class = ActividadSerializer


## Ver, Actualizar y borrar actividades

class RUDActividades(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()
