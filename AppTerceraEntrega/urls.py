from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('recetas', recetas, name='Recetas'),
    path('nutricion', nutricion, name='Nutrición'),
    path('deportes', deportes, name='Deportes'),
    path('agregar_receta', agregar_receta, name='AgregarRecetas'),
    path('agregar_nutricion', agregar_nutricion, name='AgregarNutricion'),
    path('agregar_deportes', agregar_deportes, name='AgregarDeportes'),
    path('busqueda_matricula', buscar, name="BuscarMatricula"),
    # path('buscar', buscar, name="Buscar"),
    path('', inicio, name='Inicio'),    
]