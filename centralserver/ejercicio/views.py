from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'listas.html')
# Create your views here.

def list_view(request):
    return render(request, 'listas1.html')

def poke_get(request):
    return render(request, 'listas1.html')

def poke_post(request):
    return render(request, 'listas1.html')

def poke_put(request):
    return render(request, 'listas1.html')

def poke_delete(request):
    return render(request, 'listas1.html')