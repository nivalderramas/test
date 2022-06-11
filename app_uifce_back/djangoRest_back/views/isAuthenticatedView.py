from django.contrib.auth.models import User, Group
from rest_framework import views
from rest_framework.response import Response
from djangoRest_back.models import Rol, Usuario


class isAuthenticatedView(views.APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()

    def get(self, request, format=None):
        isAuth = self.request.user.is_authenticated
        userObj = Usuario.objects.get(user=self.request.user)
        userRol = userObj.idRol
        username = self.request.user.username
        response = f'El usuario {username} esta autenticado y su rol es {userRol}' if isAuth else "El usuario no esta autenticado"
        return Response(response)
