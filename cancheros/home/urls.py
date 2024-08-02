from django.urls import path,include
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('reserva/', views.reserva, name='reserva'),
    path('usuario/', views.Usuarioform, name='usuario')
    

]

