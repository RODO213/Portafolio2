from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_registro", "mensaje", "avisos"]

        #fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]