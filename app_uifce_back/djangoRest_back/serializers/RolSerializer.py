from rest_framework import serializers
from djangoRest_back.models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['rol']