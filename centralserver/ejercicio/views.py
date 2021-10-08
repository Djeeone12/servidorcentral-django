from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import requests



def index(request):
    return render(request, 'listas.html')
# Create your views here.

def list_view(request):
    return render(request, 'listas1.html')

def poke_get(request):
    return render(request, 'poke_get.html')

def poke_get_res(request):
    poke = request.GET['poke']
    url = "https://pokeapi.co/api/v2/pokemon/"
    pokeURL = url+poke
    r = requests.get(pokeURL).json()
    return JsonResponse(r, safe=False)

def poke_post(request):
    return render(request, 'listas1.html')

def poke_put(request):
    return render(request, 'listas1.html')

def poke_delete(request):
    return render(request, 'listas1.html')