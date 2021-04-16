from django.shortcuts import render
from django.http import HttpResponse

def aplicacion1(request):
    return HttpResponse("Hola mundo")
