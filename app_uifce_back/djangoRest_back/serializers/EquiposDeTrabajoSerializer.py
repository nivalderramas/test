from rest_framework import serializers
from djangoRest_back.models import EquiposDeTrabajo

class EquiposDeTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquiposDeTrabajo
        fields = ['nombre','descripcion']