from djangoRest_back.serializers import UsuarioSerializer
from djangoRest_back.models import Usuario 
from rest_framework import generics

""" Permisos para todo tipo de Usuario """

## Lista de todos los usuarios

class ListarUsuarios(generics.ListAPIView):
    queryset = Usuario.objects.all()

## Actualizar foto de perfil

class ActualizarFotoUsuario(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    ##falta crear otro serializer que solo contenga la foto


""" Permisos para Master, Coordi y admin """

## Actualizar informacion de usuario 

class ActualizarUsuario(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


""" Permisos para admin """

## Creacion de usuarios

class CrearUsuario(generics.CreateAPIView):
    serializer_class = UsuarioSerializer

## Borrar usuarios

class BorrarUsuario(generics.DestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()