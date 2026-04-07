from django.contrib import admin
from producto.models import Producto




# admin.site.register(Producto)
# admin.site.register([Producto, asd, qwe ,123 ])
# admin.site.register(asd)
# admin.site.register(qwe)
# admin.site.register(123)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    list_filter = ['nombre']
    search_fields = ['nombre']

admin.site.register(Producto, ProductoAdmin)