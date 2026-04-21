from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class CreacionUsuario(UserCreationForm):
    password1 = forms.CharField(label='Contrasenia', help_text="", widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', help_text="", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {"username": ""}
        labels = {"username": "Nombre de usuario", "email": "Email"}

    # revisar porque mostramos esto en clase 
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['password1'].help_text = ""
    #     self.fields['password2'].help_text = ""
    
class ActualizarPerfil(UserChangeForm):
    password = None
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'fecha_nacimiento', 'avatar']
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Email",
            # "fecha_naciemiento": "Fecha Nacimiento",
            }
        # widgets = {
        #     "fecha_nacimiento": forms.DateInput(attrs={'type': 'date'}),
        #     }
        
class CambiarPass(PasswordChangeForm):
    ...
    
    # class Meta:
    #     model = User
    #     # label = {
            
    #     # }
    #     help_texts = {
    #         "old_password": '',
    #         "new_password1": '',
    #         "new_password2": '',
    #     }