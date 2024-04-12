from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("<h2>Sales 2024</h2>")

def list_view(request):
    contexto_dict = {
        'productos': {
            "Jersey Madrid - V001",
            "Jersey PSG - V002",
            "Jersey Barcelona - V003",
            "Jersey City - V004",
            "Jersey Arsenal - V005"
        }
    }
    return render(request, "list.html", contexto_dict)

def search_view(request, nombre_usuario):
    return HttpResponse(f"<h2>Productos comprados por: {nombre_usuario} </h2>")