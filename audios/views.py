from django.shortcuts import render
from .models import Audios

# Create your views here.

def audios(request):
    max_audios = 20
    audios = Audios.objects.all()
    audios_ = ""
    index = 0
    
    for i in range(len(audios)):
        
        if i >= max_audios:
            break
        
        audios_ += f""" 
            <div class="containerAudio">
                <label for="" class="audioName"> {audios[i].created} {audios[i].titulo}</label>
                <audio controls src="{audios[i].audio.url}" class="audioControl"></audio>
            </div>
        """
        index = i
    
    audios_dic ={
        "audios_":audios_, 
        "index":index, 
        "audios":audios, 
        "max_audios":max_audios
    }

    return render(request, 'audios/audios.html', audios_dic)


def mas_audios(request, index):
    max_audios = 20
    audios = Audios.objects.all()
    audios_ = ""
    index_ = index

    while index_ <= index+max_audios and index_ < len(audios):
        
        index_+=1

        if index_ >= len(audios):
            break
        
        audios_ += f""" 
            <div class="containerAudio">
                <label for="" class="audioName"> {audios[index_].created} {audios[index_].titulo}</label>
                <audio controls src="{audios[index_].audio.url}" class="audioControl"></audio>
            </div>
        """    
        

        
    last_index = (index - max_audios)-1

    if last_index < 0:
        last_index = 0

    mas_audios_dic = {
        "audios_":audios_,
        "index_":index_,
        "audios":audios, 
        "index":index, 
        "last_index":last_index,
        "max_audios":max_audios
    }

    return render(request, "audios/mas_audios.html", mas_audios_dic)
