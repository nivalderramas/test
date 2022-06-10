from djangoRest_back.serializers import EquiposDeTrabajoSerializer
from djangoRest_back.models import EquiposDeTrabajo
from rest_framework import generics


""" Permisos para todo tipo de Usuario """

## Lista de los equipos de trabajo 

class ListarEquiposTrabajo(generics.ListAPIView):
    queryset = EquiposDeTrabajo.objects.all()

""" Permisos para Coordi y admin """

## Creacion de equipos de trabajo

class CrearEquiposTrabajo(generics.CreateAPIView):
    serializer_class = EquiposDeTrabajoSerializer

## Ver, Actualizar y borrar equipos de trabajo

class RUDEquiposTrabajo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EquiposDeTrabajoSerializer
    queryset = EquiposDeTrabajo.objects.all()