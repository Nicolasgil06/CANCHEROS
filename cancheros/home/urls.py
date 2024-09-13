from django.urls import path,include
from . import views 
from .views import login_view, logout_view
from .views import mis_reservas


urlpatterns = [
    path('', views.index, name='index'),
    path('reserva/', views.reserva, name='reserva'),
    path('usuario/', views.usuario, name='usuario'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('inicio/', views.index, name='inicio'),
    path('cancelar_reserva/<int:id_reserva>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('mis_reservas/', views.mis_reservas, name='mis_reservas') 
    

]

