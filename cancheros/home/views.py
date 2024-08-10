from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from .models import Usuario
from .models import Reserva
from .forms import UsuarioForm
from .forms import ReservaForm
from django.http import HttpResponse


#aca se renderisa la pagina web en el index de html
def index(request):
    return render(request, 'index.html')

def reserva(request):    
    formulario = ReservaForm(request.POST or None)
    return render(request, 'reserva.html', {'formulario':formulario})

def usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'UsuarioForm.html',{'usuarios':usuarios})

def Usuarioform(request):
    print("Entrando a la vista Usuarioform_view") 
    if request.method == 'POST':
        form = Usuarioform(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.nombre_apellido = request.POST['nombre_apellido']
            usuario.telefono =request.POST['telefono']
            usuario.correo = request.POST['correo']
            usuario.id_documento = request.POST['id_documento']
            usuario.numero_documento = request.POST['numero_documento']
            usuario.id_rol = request.POST['id_rol']            
            usuario.save()
            messages.success(request, 'Guardado!')
            return redirect('usuario')

        else:
            messages.error(request, form.errors)
            return redirect('usuario')
    else:
        # Obtener los registros de Tipo_Documento y Rol
        resultsTipoDoc = models.TipoDocumento.objects.all()
        resultsRol = models.Rol.objects.all().order_by('nombre_rol')

        print("Tipos de Documento:", resultsTipoDoc)  # Agrega esto para verificar si los datos se obtienen correctamente
        print("Roles:", resultsRol)  # Agrega esto para verificar si los datos se obtienen correctamente

        # Renderizar la plantilla con los datos
        return render(request, "UsuarioForm.html", context={'tipodoc': resultsTipoDoc, 'lstRol': resultsRol})


#si el método es post es decir envió de información se capturan los datos se guardan en la base de datos
#  y se muestra una pagina de registro exitoso/tutorial el poder de django
""" def formulario_reserva(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        reserva_form = ReservaForm(request.POST)
        cancha_reserva_form = CanchaReservaForm(request.POST)

        if usuario_form.is_valid() and reserva_form.is_valid() and cancha_reserva_form.is_valid():
            usuario = usuario_form.save()
            reserva = reserva_form.save(commit=False)
            reserva.id_usuario = usuario
            reserva.save()
            cancha_reserva = cancha_reserva_form.save(commit=False)
            cancha_reserva.id_reserva = reserva
            cancha_reserva.save()
            return redirect('exito')
   #si la petición No es Post carga formularios para mostrarlos  / tutorial apps django   
    else:
        usuario_form = UsuarioForm()
        reserva_form = ReservaForm()
        cancha_reserva_form = CanchaReservaForm()

    return render(request, 'formulario_reserva.html', {'usuario_form': usuario_form, 'reserva_form': reserva_form, 'cancha_reserva_form': cancha_reserva_form}) """