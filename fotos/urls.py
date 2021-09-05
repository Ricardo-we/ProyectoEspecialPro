from django.urls import path
from . import views

urlpatterns = [
    path('', views.fotos, name="Fotos"),
    path('mas_fotos/<int:index>/', views.mas_fotos, name="Mas_fotos")
]