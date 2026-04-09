from django.urls import path
from sucursales.views import ListadoSucursales, CrearSucursal, ActualizarSucursal, DetalleSucursal, EliminarSucursal

app_name = 'sucursales'

urlpatterns = [
    path('', ListadoSucursales.as_view(), name='listado'),
    path('crear/', CrearSucursal.as_view(), name='crear'),
    path('<int:pk>/', DetalleSucursal.as_view(), name='detalle'),
    path('<int:pk>/actualizar/', ActualizarSucursal.as_view(), name='actualizar'),
    path('<int:pk>/eliminar/', EliminarSucursal.as_view(), name='eliminar'),
]
