from rest_framework import serializers
from djangoRest_back.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','email','RAG','pregrado','foto']