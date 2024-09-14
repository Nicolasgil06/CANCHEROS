# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cancha(models.Model):
    id_cancha = models.IntegerField(primary_key=True)
    cancha_zonal = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancha'


class CanchaReserva(models.Model):
    id_cancha_reserva = models.IntegerField(primary_key=True)
    id_cancha = models.ForeignKey(Cancha, models.DO_NOTHING, db_column='id_cancha', blank=True, null=True)
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva')

    class Meta:
        managed = False
        db_table = 'cancha_reserva'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HomeCancha(models.Model):
    id = models.BigAutoField(primary_key=True)
    cancha_zonal = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'home_cancha'


class HomeCanchareserva(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_cancha = models.ForeignKey(HomeCancha, models.DO_NOTHING)
    id_reserva = models.ForeignKey('HomeReserva', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'home_canchareserva'


class HomeReserva(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateTimeField()
    num_jugadores = models.IntegerField()
    petos = models.IntegerField()
    balones = models.IntegerField()
    id_usuario = models.ForeignKey('HomeUsuario', models.DO_NOTHING)
    id_deporte = models.ForeignKey('HomeTipodeporte', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'home_reserva'


class HomeRol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'home_rol'


class HomeTipoDocumento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre_tipo_documento = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'home_tipo_documento'


class HomeTipodeporte(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_deporte = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'home_tipodeporte'


class HomeUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    correo = models.CharField(max_length=254)
    numero_documento = models.IntegerField()
    id_documento = models.ForeignKey(HomeTipoDocumento, models.DO_NOTHING)
    id_rol = models.ForeignKey(HomeRol, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'home_usuario'


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    num_jugadores = models.IntegerField(blank=True, null=True)
    petos = models.IntegerField(blank=True, null=True)
    balones = models.IntegerField(blank=True, null=True)
    id_deporte = models.ForeignKey('TipoDeporte', models.DO_NOTHING, db_column='id_deporte', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    arbitraje = models.IntegerField(blank=True, null=True)
    color_uniforme = models.CharField(max_length=20, blank=True, null=True)
    id_cancha = models.ForeignKey(Cancha, models.DO_NOTHING, db_column='id_cancha', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class TipoDeporte(models.Model):
    id_deporte = models.IntegerField(primary_key=True)
    nombre_deporte = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_deporte'


class TipoDocumento(models.Model):
    id_documento = models.IntegerField(primary_key=True)
    nombre_tipo_documento = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=60, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    numero_documento = models.CharField(max_length=60, blank=True, null=True)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol', blank=True, null=True)
    id_documento = models.ForeignKey(TipoDocumento, models.DO_NOTHING, db_column='id_documento', blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
