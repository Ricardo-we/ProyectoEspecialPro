from django.shortcuts import render,redirect
from .models import Cartas

def cartas(request):
    max_cartas = 20
    cartas = Cartas.objects.all()
    carta = ""
    index = 0
    
    for i in range(len(cartas)):
        
        if i >= max_cartas:
            break

        carta+=f"""
        <div>
            <h2 class="titulo_carta3" style="color: red;">{cartas[i].titulo}</h2>
            <p class="carta3">{cartas[i].contenido}</p>
            <span class="finalCartas" style="color: gold;">{cartas[i].final}</span>
        </div>
        """
        index = i

    cartas_dic = {"cartas":cartas,"index":index, "carta":carta, "max_cartas":max_cartas}

    return render(request, "cartas/cartas.html", cartas_dic)


def mas_cartas(request, index):
    max_cartas = 20
    cartas = Cartas.objects.all()
    carta = ""
    index_ = index

    while index_ < index + max_cartas and index_ < len(cartas):
        
        if index_ > len(cartas):
            break

        carta+=f"""
        <div>
            <h2 class="titulo_carta3" style="color: red;">{cartas[index_].titulo}</h2>
            <p class="carta3">{cartas[index_].contenido}</p>
            <span class="finalCartas" style="color: gold;">{cartas[index_].final}</span>
        </div>
        """

        index_+=1

    last_index = (index - max_cartas)-1      

    if (last_index < 0):
        last_index = 0

    index=index_

    mas_cartas_dic = {
        "cartas":cartas, 
        "index":index, 
        "carta":carta, 
        "max_cartas":max_cartas, 
        "last_index":last_index
    }

    return render(request, "cartas/mas_cartas.html", mas_cartas_dic)