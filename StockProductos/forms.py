from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class NuevoProcesadorForm(forms.ModelForm):
    class Meta:
        model = Procesador
        fields = ['marca', 'modelo', 'precio', 'descripcion']
    
class NuevoPlacaVideoForm(forms.ModelForm):
    class Meta:
        model = PlacaVideo
        fields = ['marca', 'modelo', 'precio', 'descripcion']
    
class NuevoTecladoForm(forms.ModelForm):
    class Meta:
        model = Teclado
        fields = ['marca', 'modelo', 'precio', 'descripcion']
        
class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]    
        
class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
