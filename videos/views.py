from django.shortcuts import render
from .models import Videos

# Create your views here.
def videos(request):
    max_videos = 20
    videos = Videos.objects.all()
    index = 0
    video = ""

    for i in range(len(videos)):
        
        index = i        

        if i+1 > max_videos or i > len(videos):
            break 

        video+=f"""
        <div class="containerVideo">
            <h1 class="videoTitle">{videos[i].created} {videos[i].titulo}</h1>
            <video controls src="{videos[i].video.url}" width="500px" class="video"height="400px">
            </video>
        </div>
        """    

    context = {
        "max_videos":max_videos,
        "videos":videos,
        "index":index,
        "video":video  
    }

    return render(request, 'videos/videos.html', context)



def mas_videos(request, index):
    max_videos = 20
    videos = Videos.objects.all()
    video = ""
    index_ = index

    while index_ < index + max_videos and index_ < len(videos):
        
        if index_ > len(videos):
            break

        video+=f"""
        <div class="containerVideo">
            <h1 class="videoTitle">{videos[index_].created} {videos[index_].titulo}</h1>
            <video controls src="{videos[index_].video.url}" width="500px" class="video"height="400px">
            </video>
        </div>
        """

        index_+=1

    last_index = index - max_videos      

    if (last_index < 0):
        last_index = 0

    index=index_

    context = {
        "videos": videos, 
        "index": index, 
        "video": video, 
        "max_videos":max_videos, 
        "last_index":last_index,
    }

    return render(request, "videos/mas_videos.html", context)