from django.shortcuts import render
from .models import Fotos
# Create your views here.
def fotos(request):
    max_fotos = 20
    fotos = Fotos.objects.all()
    foto = ""
    index = 0

    for i in range(len(fotos)):
        index = i
        if i >= max_fotos:
            break
        
        foto+=f"""
        <div class="imgcontainer" id="imgVar">
            <h1 class="titulosFotos">{fotos[i].created} {fotos[i].titulo}</h1>
            <img src="{fotos[i].foto.url}" class="imagen">
        </div> 
        """
    
    return render(request, "fotos/fotos.html",{"foto":foto, "index":index, "fotos":fotos,"max_fotos":max_fotos})

def mas_fotos(request, index):
    max_fotos = 20
    fotos = Fotos.objects.all()
    foto = ""
    index_ = index

    while index_ < index + max_fotos and index < len(fotos):

        if index_ >= len(fotos):
            break

        foto+=f"""
        <div class="imgcontainer" id="imgVar">
            <h1 class="titulosFotos">{fotos[index_].created} {fotos[index_].titulo}</h1>
            <img src="{fotos[index_].foto.url}" class="imagen">
        </div> 
        """

        index_+=1

    last_index = (index - max_fotos)-1
    
    if (last_index < 0):
        last_index = 0

    index = index_

    mas_fotos_dic = {"foto":foto, "index":index, "fotos":fotos, "max_fotos":max_fotos, "last_index":last_index}
    
    return render(request, "fotos/mas_fotos.html",mas_fotos_dic)
