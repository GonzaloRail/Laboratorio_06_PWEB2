from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from models import Tareas
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html',{
            'form' : UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render (request, 'signin.html', {
                    'form': UserCreationForm,
                    'error' : 'el nombre de usuario no esta disponible'
                })
            return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'las contraseñas no coiciden'
            })    
        
def tareas(request):
    tareas = Tareas.objects.filter(user=request.user, completado__isnull=True)
    return render(request, 'tareas.html', {
        'tareas': tareas,
    })