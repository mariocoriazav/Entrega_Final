from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Venta, Serie
from .forms import VentaSearchForm, CodigoCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

@login_required
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
        return detail_codigo_view(request, nuevo_codigo.id)

    


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


@login_required
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
        form = VentaSearchForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data["nombre_usuario"]
        codigos_del_usuario = Venta.objects.filter(nombre_usuario=nombre_usuario).all()    
        contexto_dict = {"todos_los_codigos": codigos_del_usuario}
        
        return render(request, "sales/list.html", contexto_dict)
    

def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "sales/login.html", {"login": form})


from django.contrib.auth.forms import UserCreationForm


def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "sales/crear_usuario.html", {"form": form})


from django.contrib.auth import logout


def user_logout_view(request):
    logout(request)
    return redirect("login")