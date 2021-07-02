from django.shortcuts import render, redirect
from .forms import ColaboradoresForm
from .models import Colaboradores
# Create your views here.

def formulario(request):
    return render(request, 'formulario.html')

def form_colaboradores(request):
    if request.method =='POST':
        colab=ColaboradoresForm(request.POST)
        if colab.is_valid():
            colab.save()
            return redirect('formulario')
    else:
        colab=ColaboradoresForm()
    return render(request, 'anubis/formulario.html', {'colab': colab})

def VerColaboradores(request):
    colabb = Colaboradores.objects.all()
    return render(request, 'anubis/mostrar.html', context={'colabb':colabb})

def modColaborador(request,id):
    mod = Colaboradores.objects.get(rut=id)

def delColaborador(request,id):
    dele = Colaboradores.objects.get(rut=id)
    dele.delete()
    return redirect('mostrar')