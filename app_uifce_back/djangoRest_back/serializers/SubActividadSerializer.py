from rest_framework import serializers
from djangoRest_back.models import SubActividad

class SubActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubActividad
        fields = ['nombre','descripcion','fechaInicio','fechaFin','tiempoEjecucion','porcentaje']