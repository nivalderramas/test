from ast import Sub
from django.db import models
from django.contrib.auth.models import User


class Rol(models.Model):
    rol = models.CharField(max_length=45)

    def __str__(self):
        return str(self.rol)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"


class EquiposDeTrabajo(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=350)

    def __str__(self):
        return str(self.nombre) + ' - ' + str(self.descripcion)


class Estado(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return str(self.nombre)


class Actividad(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    tiempoEjecucion = models.IntegerField()
    equiposDeTrabajo = models.ForeignKey(EquiposDeTrabajo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre) + ' - ' + str(self.descripcion) + ' - ' + str(self.fechaInicio) + ' - ' + str(
            self.fechaFin) + ' - ' + str(self.tiempoEjecucion)


class SubActividad(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    tiempoEjecucion = models.DurationField()
    porcentaje = models.FloatField()
    idActividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    idEstado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.nombre) + ' - ' + str(self.descripcion) + ' - ' + str(self.fechaInicio) + ' - ' + str(
            self.fechaFin) + ' - ' + str(self.tiempoEjecucion) + ' - ' + str(self.porcentaje)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    RAG = models.IntegerField()
    idRol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    foto = models.ImageField(null=True, blank=True)
    informeDePago = models.CharField(max_length=300, null=True, blank=True)
    informesProcesoSeleccion = models.CharField(max_length=300, null=True, blank=True)
    llamadosDeAtencion = models.CharField(max_length=45, null=True, blank=True)
    despido = models.CharField(max_length=300, null=True, blank=True)
    pregrado = models.CharField(max_length=45, null=True, blank=True)
    idEquiposDeTrabajo = models.ForeignKey(EquiposDeTrabajo, null=True, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)


class Asignacion(models.Model):
    idSubActividad = models.ForeignKey(SubActividad, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idSubActividad) + ' ' + str(self.idUsuario)
