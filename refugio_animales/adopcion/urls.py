from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.home), name='home'),
    path('adopcion/verAdopcion/', login_required(views.SolicitudList.as_view()), name='verAdopcion'),
    path('adopcion/nuevaSolicitud/', login_required(views.SolicitudCreate.as_view()), name='nuevaSolicitud'),
    path('adopcion/editarSolicitud/<pk>', login_required(views.SolicitudUpdate.as_view()), name='editarSolicitud'),
    path('adopcion/eliminarSolicitud/<pk>', login_required(views.SolicitudDelete.as_view()), name='eliminarSolicitud'),
]
