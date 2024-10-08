# Generated by Django 5.0.6 on 2024-06-25 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancha_zonal', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_deporte', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('num_jugadores', models.IntegerField()),
                ('petos', models.IntegerField()),
                ('balones', models.IntegerField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
                ('id_deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tipodeporte')),
            ],
        ),
        migrations.CreateModel(
            name='CanchaReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cancha')),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.reserva')),
            ],
        ),
    ]
