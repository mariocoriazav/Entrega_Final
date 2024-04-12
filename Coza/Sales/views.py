from django.shortcuts import render
from django.http import HttpResponse
from .models import Venta

# Create your views here.

def home_view(request):
    return HttpResponse("<h2>Sales 2024</h2>")


def list_view(request):
    venta = Venta.objects.all()
    contexto_dict = {'ventas': venta}
    return render(request, "list.html", contexto_dict)

def search_view(request, nombre_usuario):
    return HttpResponse(f"<h2>Productos comprados por: {nombre_usuario} </h2>")




def create_view(request, nombre_usuario, codigo):

    venta = Venta.objects.create(nombre_usuario=nombre_usuario, codigo=codigo)

    return HttpResponse(f"Resultado: {venta}")
