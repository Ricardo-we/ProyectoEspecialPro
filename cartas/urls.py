from django.urls import path
from . import views

urlpatterns = [
    path('', views.cartas, name="Cartas"),
    path('mas_cartas/<int:index>/', views.mas_cartas, name="Mas_cartas")
]