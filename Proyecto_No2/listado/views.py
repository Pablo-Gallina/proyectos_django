from django.shortcuts import render
from .forms import AgregarTarea

tareas = ['Limpiar', 'Investigar', 'Estudiar']
# Create your views here.
def home(request):
    context = {'tareas': tareas}
    return render(request, 'lista/index.html', context)
def add(request):
    if request.method == 'POST':
        form = AgregarTarea(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data['tarea']
            tareas.append(tarea)
    else:
        form = AgregarTarea()
    context = {'form': form}
    return render(request, 'lista/add.html', context)