from django import forms
from sucursales.models import Sucursal

class FormularioActualizarSucursal(forms.ModelForm):
    # fecha_apertura = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Sucursal
        fields = ['nombre', 'fecha_apertura']
        widgets = {
            'fecha_apertura': forms.DateInput(attrs={'type': 'date'})
        }
        

class BusquedaSucursal(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)