from django.shortcuts import render, redirect
from .forms import UsuarioForm, ReservaForm, CanchaReservaForm
#aca se renderisa la pagina web en el index de html
def index(request):
    return render(request, 'index.html')

def reserva(request):
    return render(request, 'reserva.html')

#si el método es post es decir envió de información se capturan los datos se guardan en la base de datos
#  y se muestra una pagina de registro exitoso/tutorial el poder de django
def formulario_reserva(request):
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

    return render(request, 'formulario_reserva.html', {'usuario_form': usuario_form, 'reserva_form': reserva_form, 'cancha_reserva_form': cancha_reserva_form})