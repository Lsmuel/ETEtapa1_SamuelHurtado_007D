from django.shortcuts import render, redirect
from .models import Colaboradores
# Create your views here.

def formulario(request):
    return render(request, 'formulario.html')
