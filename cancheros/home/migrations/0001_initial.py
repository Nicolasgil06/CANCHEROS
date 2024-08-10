# Generated by Django 5.0.6 on 2024-06-25 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Documento',
            fields=[
                ('id_documento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_documento', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=45)),
                ('correo', models.EmailField(max_length=254)),
                ('numero_documento', models.IntegerField()),
                ('id_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tipo_documento')),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.rol')),
            ],
        ),
    ]