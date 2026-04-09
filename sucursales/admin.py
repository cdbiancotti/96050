from django.contrib import admin
from sucursales.models import Sucursal


class SucursalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'fecha_apertura']
    list_filter = ['fecha_apertura']
    search_fields = ['nombre']

admin.site.register(Sucursal, SucursalAdmin)