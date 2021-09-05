from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="Home"),
    path('juegos/corazon_volon/', views.juego1, name="Juego1"),
    path('juegos/corazon_esquivador/', views.juego2, name="Juego2"),
    path('juegos/busca_el_corazon/', views.juego3, name="Juego3"),
    path('juegos/pong_love/', views.juego4, name="Juego4"),
    path('juegos/snake/', views.juego5, name="Juego5"),
    path('juegos/corazon_volor_xl/', views.juego6, name="Juego6"),
    path('juegos/heart_adventures/', views.juego7, name="Juego7"),
]