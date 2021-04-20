from django.urls import path
from . import views

urlpatterns = [
    path('nuevoUsuario/', views.RegistroUsuario.as_view(), name='nuevoUsuario'),
]
