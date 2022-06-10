from rest_framework import serializers
from djangoRest_back.models import Actividad

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['nombre','descripcion','fechaInicio','fechaFin','tiempoEjecucion','equiposDeTrabajo']