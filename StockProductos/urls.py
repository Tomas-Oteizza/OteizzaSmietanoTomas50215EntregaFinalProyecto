from django.urls import path 
from .views import *

from django.contrib.auth.views import LogoutView 

urlpatterns = [
    #---------medu lateral:
    path('', home, name="home"),
    path('procesador', Procesadorlist.as_view(), name="procesador"),
    path('placaVideo', PlacaVideoList.as_view(), name="placaVideo"),
    path('teclado', TecladoList.as_view(), name="teclado"),
    path('gabinete', GabineteList.as_view(), name="gabinete"),
    path('aboutMe', aboutMe, name="aboutMe"), 
    
    #---------Procesadores:
    path('ProcesadorCreate', ProcesadorCreate.as_view(), name="ProcesadorCreate"),
    path('actualizarProcesador/<int:pk>/', ProcesadorUpdate.as_view(), name="actualizarProcesador"), 
    path('deleteProcesador/<int:pk>/', ProcesadorDelete.as_view(), name="deleteProcesador"),
    path('buscarProcesadores', buscarProcesadores, name="buscarProcesadores"),
    path('encontrarProcesadores', encontrarProcesadores, name="encontrarProcesadores"),
    
    #----------------Placa de video:
    path('PlacaVideoCreate', PlacaVideoCreate.as_view(), name="PlacaVideoCreate"),
    path('actualizarPlacaVideo/<int:pk>/', PlacaVideoUpdate.as_view(), name="actualizarPlacaVideo"), 
    path('deletePlacaVideo/<int:pk>/', PlacaVideoDelete.as_view(), name="deletePlacaVideo"),
    path('buscarPlacasVideo', buscarPlacasVideo, name="buscarPlacasVideo"),
    path('encontrarPlacasVideo', encontrarPlacasVideo, name="encontrarPlacasVideo"),
    
    #---------Teclados:
    path('TecladoCreate', TecladoCreate.as_view(), name="TecladoCreate"),
    path('actualizarTeclado/<int:pk>/', TecladoUpdate.as_view(), name="actualizarTeclado"), 
    path('deleteTeclado/<int:pk>/', TecladoDelete.as_view(), name="deleteTeclado"),
    path('buscarTeclados', buscarTeclados, name="buscarTeclados"),
    path('encontrarTeclados', encontrarTeclados, name="encontrarTeclados"),
    
    #---------Gabinetes::
    path('GabineteCreate', GabineteCreate.as_view(), name="GabineteCreate"),
    path('actualizarGabinete/<int:pk>/', GabineteUpdate.as_view(), name="actualizarGabinete"), 
    path('deleteGabinete/<int:pk>/', GabineteDelete.as_view(), name="deleteGabinete"),
    path('buscarGabinete', buscarGabinete, name="buscarGabinete"),
    path('encontrarGabinete', encontrarGabinete, name="encontrarGabinete"),
    
    #---------------------------Perfiles: 
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="StockProductos/logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),
    
    #--------------------Edicion de perfiles:
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
]
 

    
    