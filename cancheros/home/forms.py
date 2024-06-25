from . import models 
from django import forms


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields= ['nombre_apellido', 
                 'telefono',  
                 'correo',
                 'id_documento',
                 'numero_documento',
                 'id_rol',
                 ]
        