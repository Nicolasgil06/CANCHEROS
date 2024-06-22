from django import forms
from .models import Usuario, Reserva, CanchaReserva

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_apellido', 'telefono', 'correo', 'id_documento']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha', 'hora', 'num_jugadores', 'petos', 'balones', 'id_deporte']

class CanchaReservaForm(forms.ModelForm):
    class Meta:
        model = CanchaReserva
        fields = ['id_cancha']
