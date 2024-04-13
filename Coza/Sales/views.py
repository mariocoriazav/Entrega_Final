from django.shortcuts import render
from django.http import HttpResponse
from .models import Venta

# Create your views here.

def home_view(request):
    return render(request, "sales/home.html")   

def detail_view(request, sales_id):
    venta = Venta.objects.get(id=sales_id)
    contexto_dict = {"venta": venta}
    return render(request, "sales/detail.html", contexto_dict)


def list_view(request):
    ventas = Venta.objects.all()
    contexto_dict = {'ventas': ventas}

    return render(request, "sales/list.html", contexto_dict)

def search_view(request, nombre_usuario):
    codigos_del_usuario = Venta.objects.filter(nombre_usuario=nombre_usuario).all()
    contexto_dict = {'ventas': codigos_del_usuario}

    return render(request, "sales/list.html", contexto_dict)
  

def create_view(request, nombre_usuario, codigo):

    venta = Venta.objects.create(nombre_usuario=nombre_usuario, codigo=codigo)

    return HttpResponse(f"Resultado: {venta}")
