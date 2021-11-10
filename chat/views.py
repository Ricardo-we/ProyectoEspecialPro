from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse 
from .models import Users, Messages

# Create your views here.


def login(request):
    return render(request, 'chat/login.html', {})

def check_user(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        user_exists = Users.objects.filter(username=username)     
        
        if user_exists.exists():
            return redirect(f'/chat/chat_gatitos/{username}/')

        new_user = Users(username=username)
        new_user.save()
        return redirect(f'/chat/chat_gatitos/{username}/')

def save_message(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        message = request.POST.get('message')
        print(username, message)
        try:
            new_message = Messages(username=username, message=message)
            new_message.save()
        except:
            return HttpResponse("Internal server error")
        return HttpResponse("Done")

    return HttpResponse("Error")

def chat(request, username):
    return render(request, 'chat/chat.html', {'username': username})

def get_messages(request):
    messages = Messages.objects.all()
    messages_dic = {
        'usernames':[] ,
        'messages': []
    }

    for message in messages:
        messages_dic['usernames'].append(message.username)
        messages_dic['messages'].append(message.message)

    return JsonResponse(messages_dic)