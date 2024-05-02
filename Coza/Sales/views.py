from django.shortcuts import render
from django.http import HttpResponse
from .models import Venta, Serie
from .forms import VentaSearchForm, VentaCreateForm, CodigoCreateForm

# Create your views here.

def create_codigo_with_form_view(request):
    if request.method == "GET":
        contexto = {"create_form": CodigoCreateForm()}
        return render(request, "sales/form-create-codigo.html", contexto)
     
    elif request.method == "POST":
        form = CodigoCreateForm(request.POST)
        if form.is_valid():
        nombre = form.cleaned_data['nombre']
        disponible = form.cleaned_data['disponible']
        capacidad = form.cleaned_data['capacidad']
        nuevo_codigo = Serie(nombre=nombre, disponible=disponible, capacidad=capacidad)
        nuevo_codigo.save()
        return detail_codigo_view(nuevo_codigo.id)

    


def create_with_form_view(request):
    contexto = {"create_form": VentaCreateForm() }
    return render(request, "sales/form-create.html", contexto)

def home_view(request):
    return render(request, "sales/home.html")   

def detail_view(request, sales_id):
    venta = Venta.objects.get(id=sales_id)
    contexto_dict = {"venta": venta}
    return render(request, "sales/detail.html", contexto_dict)


def detail_codigo_view(request, codigo_id):
    codigo = Serie.objects.get(id=codigo_id)
    contexto_dict = {"codigo": codigo}
    return render(request, "sales/detail-codigo.html", contexto_dict)


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


def search_with_form_view(request):
    if request.method == "GET":
        form = VentaSearchForm()
        return render(request, "sales/form-search.html", context={"search_form":form})
    elif request.method == "POST":
        nombre_usuario = "ana"
        contexto_dict = {'ventas': codigos_del_usuario}
        codigos_del_usuario = Venta.objects.filter(nombre_usuario=nombre_usuario).all()
        return render(request, "sales/list.html", contexto_dict)