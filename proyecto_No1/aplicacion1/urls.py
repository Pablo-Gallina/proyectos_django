from django.urls import path
from . import views

urlpatterns = [
    path('', views.aplicacion1, name='aplicacion1'),
    #path('<str:nombre>/', views.saludar, name='saludo'),
    path('moneda/', views.moneda, name='moneda'),
]
