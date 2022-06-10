from rest_framework import serializers
from djangoRest_back.models import Asignacion

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion