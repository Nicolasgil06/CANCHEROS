from django.urls import path,include
from . import views 
from .views import login_view, logout_view


urlpatterns = [
    path('', views.index, name='index'),
    path('reserva/', views.reserva, name='reserva'),
    path('usuario/', views.usuario, name='usuario'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('inicio/', views.index, name='inicio'),
    path('cancelar/', views.cancelar, name='cancelar')
    
    

]

