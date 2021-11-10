from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name="Login"),
    path('check_user/', views.check_user, name="check_user"),
    path('chat_gatitos/<str:username>/', views.chat, name="Chat"),
    path('get_messages/', views.get_messages, name="get_messages"),
    path('new_message/', views.save_message, name="new_message")
]