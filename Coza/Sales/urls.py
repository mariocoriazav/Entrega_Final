from django.contrib import admin
from django.urls import path
from .views import home_view, detail_view, list_view, search_view, create_view



urlpatterns = [
    path("", home_view),
    path("detail/<sales_id>", detail_view),
    path("list/", list_view),
    path("buscar/<nombre_usuario>", search_view),
    path("crear/<nombre_usuario>/<codigo>", create_view),

    
]
