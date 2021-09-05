from django.urls import path
from . import views

urlpatterns = [
    path('', views.audios ,name="Audios"),
    path('mas_audios/<int:index>/', views.mas_audios, name="Mas_audios")
]