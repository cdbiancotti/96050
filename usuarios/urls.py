from django.urls import path
from usuarios.views import iniciar_sesion, registrarse, perfil
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='usuarios/cerrar_sesion.html'), name='cerrar_sesion'),
    path('registro/', registrarse, name='registro'),
    path('perfil/', perfil, name='perfil'),
]
