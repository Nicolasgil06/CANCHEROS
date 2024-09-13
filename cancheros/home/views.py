from django.contrib.auth.hashers import make_password
from  django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .import models
from  django.contrib import messages
from  home.models import Reserva ,Usuario, TipoDeporte
from django.shortcuts import get_object_or_404, redirect
from .forms import UsuarioForm
from .forms import ReservaForm
from  django.http import HttpResponse
from .models import Reserva
from django.contrib import messages
from django.shortcuts import render

def login_view(request):
    print("entro al metodo")
    if request.method == 'POST':
        print("entro al post")
        username = request.POST['Username']
        password = request.POST['Password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            print("entro afirmativo")
            login(request)
            # Guardar una variable en la sesión
            request.session['nombre_usuario'] = user.nombres
            request.session['idUsuario']  = user.id_usuario
            messages.success(request, f'Bienvenido, {user.nombres}!')
            return redirect('inicio')  # Redirigir a la página de inicio u otra página
        else:
            print("entro negativo")
            messages.error(request, 'Credenciales incorrectas, intente nuevamente.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')


def mis_reservas(request):    
    id_usuario = request.session.get('idUsuario')  # Usa get para evitar KeyError    
    if id_usuario:        
        reservas = Reserva.objects.filter(id_usuario=id_usuario)
    else:
        reservas = []  # O redirige al usuario a una página de error o inicio de sesión
    return render(request, 'mis_reservas.html', {'reservas': reservas})


def index(request):
    return render(request, 'index.html')


def reserva(request):   
    
    resultsdeporte = models.TipoDeporte.objects.all().order_by('nombre_deporte') 
    resultscancha = models.Cancha.objects.all().order_by('cancha_zonal') 

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
            return render(request, 'reserva.html', context={'lstdeporte': resultsdeporte, 'lstcancha': resultscancha})
    else:
        # Renderizar la plantilla en caso de GET
        return render(request, 'reserva.html', context={'lstdeporte': resultsdeporte, 'lstcancha': resultscancha})


def login(request):   
    return render(request, 'login.html')


def usuario(request):       
    print("entra a usuario")
    print(request.method)
    form = UsuarioForm()
     # Obtener los registros de Tipo_Documento y Rol
    resultsTipoDoc = models.TipoDocumento.objects.all()
    resultsRol = models.Rol.objects.all().order_by('nombre_rol')
    if request.method == 'POST':
        print("entra al post")
        form = UsuarioForm(request.POST)
        if form.is_valid():             
            print("aqui paso validacion")
            usuario = form.save(commit=False)  # No guardar aún en la base de datos
            usuario.clave = make_password(form.cleaned_data['clave'])  # Encriptar la contraseña
            usuario.save()  # Ahora sí, guardar en la base de datos
            messages.success(request,'Guardado!')
            return render(request, 'Usuarioexitoso.html', context={'lstDoc': resultsTipoDoc, 'lstRol': resultsRol})
        else:    
            print("entra a errort")   
            print(form.errors)  # ayudará a ver por qué el formulario no es válido
            messages.error(request, form.errors)
        return render(request, 'usuario.html', context={'lstDoc': resultsTipoDoc, 'lstRol': resultsRol}) #esto lo agrege por sug de chat
            
    else:        
        print("entra a devolverso")
        # Renderizar la plantilla con los datos
        return render(request, 'usuario.html', context={'lstDoc': resultsTipoDoc, 'lstRol': resultsRol})




#si el método es post es decir envió de información se capturan los datos se guardan en la base de datos
#  y se muestra una pagina de registro exitoso/tutorial el poder de django

def cancelar_reserva(request, id_reserva):
    reserva = get_object_or_404(Reserva, id_reserva=id_reserva)
    if request.method == 'POST':  # Asegúrate de que es una solicitud POST
        reserva.delete()  # Elimina la reserva de la base de datos
    return redirect('mis_reservas') 