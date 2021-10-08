from django.shortcuts import render, redirect
from .models import Arriendo
from .forms import ContactoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
#from django.contrib.auth import login as auth_login

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def contacto(request):
    data = {
        'form' : ContactoForm()
    }

    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "CONTACTO GUARDADO")

        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def arriendo(request):
    return render(request, 'app/arriendo.html')

def hotel(request):
    return render(request, 'app/hotel.html')

def tour(request):
    return render(request, 'app/tour.html')


def quienes_somos(request):
    return render(request, 'app/quienessomos.html')


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            #login(request, user)
            messages.success(request, "Registro Exitoso")
            return redirect(to="home")

        data["form"] = formulario
        
        

    return render(request, 'registration/registro.html', data)
