from django import forms
from .models import Reserva, Usuario, TipoDeporte

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
        
        
        """ from . import models
from django import forms


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields= ['nombres',
                 'apellidos', 
                 'telefono',  
                 'correo',
                 'clave',
                 'id_documento',
                 'numero_documento',
                 'id_rol'
                 ]          
class ReservaForm(forms.ModelForm):
    class Meta:
        model = models.Reserva
        fields= ['fecha', 
                 'hora',  
                 'num_jugadores',
                 'petos',
                 'balones',
                 'id_deporte',
                 'id_usuario',
                 'arbitraje',
                 'color_uniforme'
                  ]   """