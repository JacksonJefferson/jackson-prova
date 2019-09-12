from django.shortcuts import render, redirect
#from . models import Paciente
#from . forms import PacienteForm

def home(request):
    return render (request, 'home.html')