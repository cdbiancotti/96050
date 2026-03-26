
from django.urls import path
from producto.views import inicio, datos, productos, crear_producto


urlpatterns = [
    path('', inicio),
    path('datos/', datos),
    path('productos/', productos),
    path('crear_producto/', crear_producto),
]
