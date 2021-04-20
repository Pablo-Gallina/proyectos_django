from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nuevo/', views.mascota_view, name='nuevo'),
    path('listar/', views.mascota_listar, name='listar'),
    path('editar/<int:id_mascota>/', views.mascota_edit, name='editar'),
    path('eliminar/<int:id_mascota>/', views.mascota_delete, name='eliminar'),
]
