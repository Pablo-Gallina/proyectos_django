from django.shortcuts import render

tareas = ['Limpiar', 'Investigar', 'Estudiar']
# Create your views here.
def home(request):
    context = {'tareas': tareas}
    return render(request, 'lista/index.html', context)
def add(request):
    return render(request, 'lista/add.html')