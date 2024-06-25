from django.db import models


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=45)
    class Meta:
        pass

    def __str__(self):
        return str(self.nombre_rol)


class Tipo_Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre_tipo_documento = models.CharField(max_length=45)
    class Meta:
        pass

    def __str__(self):
        return str(self.nombre_tipo_documento)

class Usuario(models.Model):
    nombre_apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    correo = models.EmailField()
    id_documento = models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE)
    numero_documento = models.IntegerField()
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Cancha(models.Model):
    cancha_zonal = models.CharField(max_length=45)

class TipoDeporte(models.Model):
    nombre_deporte = models.CharField(max_length=45)

class Reserva(models.Model):
    fecha = models.DateField()
    hora = models.DateTimeField()
    num_jugadores = models.IntegerField()
    petos = models.IntegerField()
    balones = models.IntegerField()
    id_deporte = models.ForeignKey(TipoDeporte, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class CanchaReserva(models.Model):
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    id_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
