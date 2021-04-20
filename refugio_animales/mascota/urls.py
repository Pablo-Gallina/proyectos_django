from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nuevo/', views.MascotaCreate.as_view(), name='nuevo'),
    path('listar/', views.MascotaList.as_view(), name='listar'),
    path('editar/<pk>/', views.MascotaUpdate.as_view(), name='editar'),
    path('eliminar/<pk>/', views.MascotaDelete.as_view(), name='eliminar'),
]
