from django.db import models

class TipoDocumento(models.Model):
    nombre_tipo_documento = models.CharField(max_length=45)

class Usuario(models.Model):
    nombre_apellido = models.CharField(max_length=45)
    telefono = models.IntegerField()
    correo = models.EmailField()
    id_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    id_rol = models.IntegerField(default=1)

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
