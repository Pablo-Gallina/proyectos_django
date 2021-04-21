from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('lista', views.listado, name="lista"),
    path('nuevo/', login_required(views.MascotaCreate.as_view()), name='nuevo'),
    path('listar/', login_required(views.MascotaList.as_view()), name='listar'),
    path('editar/<pk>/', login_required(views.MascotaUpdate.as_view()), name='editar'),
    path('eliminar/<pk>/', login_required(views.MascotaDelete.as_view()), name='eliminar'),
]
