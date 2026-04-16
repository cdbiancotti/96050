from django import forms
from django.contrib.auth.forms import UserCreationForm
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