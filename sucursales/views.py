from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from sucursales.models import Sucursal
from django.urls import reverse_lazy
from sucursales.forms import FormularioActualizarSucursal, BusquedaSucursal
from django.contrib.auth.mixins import LoginRequiredMixin


class ListadoSucursales(ListView):
    model = Sucursal
    template_name = "sucursales/listado.html"
    context_object_name = 'sucursales'

    def get_queryset(self):
        sucursales = super().get_queryset()
        formulario = BusquedaSucursal(self.request.GET)
        if formulario.is_valid():
            nombre_parcial_a_buscar = formulario.cleaned_data['nombre']
            sucursales = sucursales.filter(nombre__icontains=nombre_parcial_a_buscar)
        return sucursales
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaSucursal()
        return context
    


class CrearSucursal(LoginRequiredMixin, CreateView):
    model = Sucursal
    template_name = "sucursales/crear.html"
    # fields = ['nombre', 'direccion', 'fecha_apertura']
    fields = "__all__"
    success_url = reverse_lazy('sucursales:listado')

class ActualizarSucursal(LoginRequiredMixin, UpdateView):
    model = Sucursal
    template_name = "sucursales/actualizar.html"
    # fields = ['nombre', 'fecha_apertura']
    form_class = FormularioActualizarSucursal
    success_url = reverse_lazy('sucursales:listado')

class EliminarSucursal(LoginRequiredMixin, DeleteView):
    model = Sucursal
    template_name = "sucursales/eliminar.html"
    success_url = reverse_lazy('sucursales:listado')

class DetalleSucursal(DetailView):
    model = Sucursal
    template_name = "sucursales/detalle.html"
