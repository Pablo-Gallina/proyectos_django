from django.shortcuts import render
from django.http import HttpResponse

def aplicacion1(request):
    #return HttpResponse("Hola mundo")
    return render(request, 'aplicacion1/index.html')

def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre}")

    