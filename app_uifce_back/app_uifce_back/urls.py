"""app_uifce_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:


Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoRest_back.views import ListarActividades, CrearActividades, RUDActividades, ListarEquiposTrabajo, CrearEquiposTrabajo, RUDEquiposTrabajo, CrearEstado, RUDEstado, CrearRol, RUDRol, ListarSubActividades, ActualizarSubActividades, CrearSubActividades, BorrarSubActividades, ListarUsuarios, ActualizarFotoUsuario, ActualizarUsuario, CrearUsuario, BorrarUsuario

urlpatterns = [
    path('admin/', admin.site.urls),

    path('list-activities/', ListarActividades.as_view()),
    path('create-activities/', CrearActividades.as_view()),
    path('RUD-activities/',RUDActividades.as_view()),

    path('list-workteams/',ListarEquiposTrabajo.as_view()),
    path('create-workteams/', CrearEquiposTrabajo.as_view()),
    path('RUD-workteams/', RUDEquiposTrabajo.as_view()),

    path('create-state/', CrearEstado.as_view()),
    path('RUD-state/', RUDEstado.as_view()),
    
    path('list-activities/', CrearRol.as_view()),
    path('create-activities/', RUDRol.as_view()),

    path('RUD-activities/',ListarSubActividades.as_view()),
    path('list-workteams/',ActualizarSubActividades.as_view()),
    path('create-workteams/', CrearSubActividades.as_view()),
    path('RUD-workteams/', BorrarSubActividades.as_view()),

    path('create-state/', ListarUsuarios.as_view()),
    path('RUD-state/', ActualizarFotoUsuario.as_view()),
    path('RUD-state/', ActualizarUsuario.as_view()),
    path('RUD-state/', CrearUsuario.as_view()),
    path('RUD-state/', BorrarUsuario.as_view())
    
]
