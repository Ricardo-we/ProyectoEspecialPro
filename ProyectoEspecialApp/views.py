from django.shortcuts import render
import datetime
import time
from .models import *

# Create your views here.
def home(request):
    contador5 = str(datetime.date.today().day)
    updates = Updates.objects.all()
    downloads = Downloads.objects.all()

    home_dic = {"contador5":contador5,"updates":updates, "downloads":downloads}
    
    return render(request, "ProyectoEspecialApp/home.html", home_dic)

def juego1(request):
    return render(request, 'ProyectoEspecialApp/juegos/un_jueguito.html', {})

def juego2(request):
    return render(request, 'ProyectoEspecialApp/juegos/juego2.html', {})    

def juego3(request):
    return render(request, 'ProyectoEspecialApp/juegos/juego3.html', {})

def juego4(request):
    return render(request, 'ProyectoEspecialApp/juegos/juego4.html', {})

def juego5(request):
    return render(request, 'ProyectoEspecialApp/juegos/juego5.html', {})

def juego6(request):
    return render(request, 'ProyectoEspecialApp/juegos/juego6.html', {})

def juego7(request):
    return render(request, 'ProyectoEspecialApp/juegos/juego8.html', {})