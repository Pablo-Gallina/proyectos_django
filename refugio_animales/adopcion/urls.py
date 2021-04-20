from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adopcion/verAdopcion/', views.SolicitudList.as_view(), name='verAdopcion'),
    path('adopcion/nuevaSolicitud/', views.SolicitudCreate.as_view(), name='nuevaSolicitud'),
    path('adopcion/editarSolicitud/<pk>', views.SolicitudUpdate.as_view(), name='editarSolicitud'),
    path('adopcion/eliminarSolicitud/<pk>', views.SolicitudDelete.as_view(), name='eliminarSolicitud'),
]
