from django.shortcuts import render, redirect
from .forms import ColaboradoresForm
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