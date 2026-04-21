from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from usuarios.forms import CreacionUsuario, ActualizarPerfil, CambiarPass
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoExtra
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST) 
        if formulario.is_valid():
            user = formulario.get_user()
            
            login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect("producto:inicio")
    else:
        formulario = AuthenticationForm()
    
    
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario_iniciar_sesion': formulario})

def registrarse(request):
    
    if request.method == "POST":
        formulario = CreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("usuarios:iniciar_sesion")
    else:
        formulario = CreacionUsuario()
    
    return render(request, 'usuarios/registro.html', {'formulario_registro': formulario})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def actualizar_perfil(request):
    
    if request.method == "POST":
        formulario = ActualizarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            request.user.infoextra.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
            if formulario.cleaned_data.get('avatar'):
                request.user.infoextra.avatar = formulario.cleaned_data.get('avatar')
            request.user.infoextra.save()
            formulario.save()
            return redirect('usuarios:perfil')
    else:
        formulario = ActualizarPerfil(
            instance=request.user, 
            initial={
                'fecha_nacimiento': request.user.infoextra.fecha_nacimiento, 
                'avatar': request.user.infoextra.avatar
            }
        )
    return render(request, 'usuarios/actualizar_perfil.html', {'formulario': formulario})


class CambioDePass(PasswordChangeView):
    template_name = 'usuarios/cambio_pass.html'
    form_class = CambiarPass
    success_url = reverse_lazy('usuarios:perfil')