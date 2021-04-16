from django.urls import path
from . import views

urlpatterns = [
    path('', views.aplicacion1, name='aplicacion1')
]
