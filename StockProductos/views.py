from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import * 


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "StockProductos/index.html")

def aboutMe(request):
    return render (request, "StockProductos/aboutMe.html")

#----------------------------------Procesadores:
class Procesadorlist(LoginRequiredMixin, ListView):
    model = Procesador

class ProcesadorCreate(LoginRequiredMixin, CreateView):
    model = Procesador
    fields = ["marca", "modelo", "stock", "precio", "descripcion"]
    success_url = reverse_lazy("procesador")
    
class ProcesadorUpdate(LoginRequiredMixin, UpdateView):
    model = Procesador
    fields = ["marca", "modelo","stock", "precio", "descripcion"]
    success_url = reverse_lazy("procesador")

class ProcesadorDelete(LoginRequiredMixin, DeleteView):
    model = Procesador
    success_url = reverse_lazy("procesador")

@login_required
def buscarProcesadores(request):
    return render(request, "StockProductos/buscarProcesadores.html")

@login_required
def encontrarProcesadores(request):
    if 'buscarProcesadores' in request.GET:
        patron = request.GET.get('buscarProcesadores', '')
        if patron:
            procesador_list = Procesador.objects.filter(modelo__icontains=patron)
            contexto = {"procesador_list": procesador_list}
            return render(request, "StockProductos/procesador_list.html", contexto)

    
    contexto = {'procesadores': Procesador.objects.all()}
    return render(request, "StockProductos/procesador.html", contexto)

#----------------------------------Placas de video:
class PlacaVideoList(LoginRequiredMixin, ListView):
    model = PlacaVideo
    
class PlacaVideoCreate(LoginRequiredMixin, CreateView):
    model = PlacaVideo
    fields = ["marca", "modelo", "stock", "precio", "descripcion"]
    success_url = reverse_lazy("placaVideo")
    
class PlacaVideoUpdate(LoginRequiredMixin, UpdateView):
    model = PlacaVideo
    fields = ["marca", "modelo", "stock", "precio", "descripcion"]
    success_url = reverse_lazy("placaVideo")

class PlacaVideoDelete(LoginRequiredMixin, DeleteView):
    model = PlacaVideo
    success_url = reverse_lazy("placaVideo")

@login_required
def buscarPlacasVideo(request):
    return render(request, "StockProductos/buscarPlacasVideo.html")

@login_required
def encontrarPlacasVideo(request):
    if 'buscarPlacasVideo' in request.GET:
        patron = request.GET.get('buscarPlacasVideo', '')
        if patron:
            placavideo_list = PlacaVideo.objects.filter(modelo__icontains=patron)
            contexto = {"placavideo_list": placavideo_list}  # Corregir la clave del diccionario
            return render(request, "StockProductos/placaVideo_list.html", contexto)

    contexto = {'placaVideo_list': PlacaVideo.objects.all()}
    return render(request, "StockProductos/placaVideo_list.html", contexto)

#----------------------------------Teclados:
class TecladoList(LoginRequiredMixin, ListView):
    model = Teclado

class TecladoCreate(LoginRequiredMixin, CreateView):
    model = Teclado
    fields = ["marca", "modelo", "stock", "precio", "descripcion"]
    success_url = reverse_lazy("teclado")
    
class TecladoUpdate(LoginRequiredMixin, UpdateView):
    model = Teclado
    fields = ["marca", "modelo", "stock", "precio", "descripcion"]
    success_url = reverse_lazy("teclado")

class TecladoDelete(LoginRequiredMixin, DeleteView):
    model = Teclado
    success_url = reverse_lazy("teclado")

login_required
def buscarTeclados(request):
    return render(request, "StockProductos/buscarTeclados.html")

login_required
def encontrarTeclados(request):
    if 'buscarTeclado' in request.GET:  
        patron = request.GET.get('buscarTeclado', '')  
        if patron:
            teclado_list = Teclado.objects.filter(modelo__icontains=patron)
            contexto = {"teclado_list": teclado_list}
            return render(request, "StockProductos/teclado_list.html", contexto)

    contexto = {'teclados': Teclado.objects.all()}
    return render(request, "StockProductos/teclado_list.html", contexto)

#----------------------------------Gabinetes:
class GabineteList(LoginRequiredMixin, ListView):
    model = Gabinete

class GabineteCreate(LoginRequiredMixin, CreateView):
    model = Gabinete
    fields = ["marca", "modelo", "stock", "precio", "descripcion"]
    success_url = reverse_lazy("gabinete")
    
class GabineteUpdate(LoginRequiredMixin, UpdateView):
    model = Gabinete
    fields = ["marca", "modelo", "stock", "precio", "descripcion"]
    success_url = reverse_lazy("gabinete")

class GabineteDelete(LoginRequiredMixin, DeleteView):
    model = Gabinete
    success_url = reverse_lazy("gabinete")

login_required
def buscarGabinete(request):
    return render(request, "StockProductos/buscarGabinete.html")

login_required
def encontrarGabinete(request):
    if 'buscarGabinete' in request.GET:  
        patron = request.GET.get('buscarGabinete', '')  
        if patron:
            gabinete_list = Gabinete.objects.filter(modelo__icontains=patron)
            contexto = {"gabinete_list": gabinete_list}
            return render(request, "StockProductos/gabinete_list.html", contexto)

    contexto = {'gabinete': Gabinete.objects.all()}
    return render(request, "StockProductos/gabinete_list.html", contexto)

#----------------------------------Perfiles:
def loginRequest(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #----------------------------Avatar:
            try:
                avatar = avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #-----------------------------------   
            return render(request, "StockProductos/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "StockProductos/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "StockProductos/registro.html", {"form": miForm} ) 

#-------------------------------------------Edicion de perfiles:
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = UserEditForm(instance=usuario)

    return render(request, "Stockproductos/editarPerfil.html", {"form": miForm} )    
   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "StockProductos/cambiarClave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #-----------------Borrar avatar viejo:
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #------------------------------------
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()

    return render(request, "StockProductos/agregarAvatar.html", {"form": miForm})
