from django.shortcuts import render, redirect;
from . import models
from django.contrib import messages
from home.models import Reserva, Usuario, TipoDeporte
from .forms import UsuarioForm
from .forms import ReservaForm
from django.http import HttpResponse
from .models import Reserva



#aca se renderisa la pagina web en el index de html
def index(request):
    return render(request, 'index.html')


def reserva(request):   
    print("entro al metodo")
    resultsdeporte = models.TipoDeporte.objects.all().order_by('nombre_deporte') 
    form = ReservaForm()

    if request.method == 'POST':        
        form = ReservaForm(request.POST)
        if form.is_valid():
            
            reserva = form.save(commit=False)
            
            # Si necesitas obtener el ID de deporte y usuario, no es necesario hacerlo manualmente aquí,
            # Django lo maneja automáticamente si los campos son correctos en el formulario.
            
            reserva.save()
                        
            messages.success(request,'Guardado!')
            return render(request, 'reservaexitosa.html')
            #return redirect('nombre_de_tu_vista') # Redirigir a la página de éxito 
        else:   
            print(form.errors)  # Esto te ayudará a ver por qué el formulario no es válido
            messages.error(request, form.errors)                 
            return render(request, 'reserva.html', context={'lstdeporte': resultsdeporte})
    else:
        # Renderizar la plantilla en caso de GET
        return render(request, 'reserva.html', context={'lstdeporte': resultsdeporte})



def usuario(request):       
    form = UsuarioForm()
     # Obtener los registros de Tipo_Documento y Rol
    resultsTipoDoc = models.TipoDocumento.objects.all()
    resultsRol = models.Rol.objects.all().order_by('nombre_rol')
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():                       
            form.save()
            messages.success(request,'Guardado!')
            return render(request, 'usuario.html', context={'lstDoc': resultsTipoDoc, 'lstRol': resultsRol})
        else:   
            messages.error(request, form.errors)
            
    else:        
        # Renderizar la plantilla con los datos
        return render(request, "usuario.html", context={'lstDoc': resultsTipoDoc, 'lstRol': resultsRol})


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