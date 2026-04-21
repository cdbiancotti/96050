from django.urls import path
from usuarios.views import iniciar_sesion, registrarse, perfil, actualizar_perfil, CambioDePass
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='usuarios/cerrar_sesion.html'), name='cerrar_sesion'),
    path('registro/', registrarse, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/actualizar/', actualizar_perfil, name='actualizar_perfil'),
    path('perfil/actualizar/pass/', CambioDePass.as_view(), name='actualizar_pass'),
]
