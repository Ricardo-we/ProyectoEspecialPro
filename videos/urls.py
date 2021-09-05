from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos, name='Videos'),
    path('mas_videos/<int:index>/', views.mas_videos, name='Mas_videos')
]