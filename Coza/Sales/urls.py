from django.contrib import admin
from django.urls import path

from .views import (
    home_view,
    detail_view,
    list_view,
    search_view,
    create_view,
    search_with_form_view,
    create_with_form_view,
    create_codigo_with_form_view,
    detail_codigo_view,
    user_creation_view,
    user_login_view,
    user_logout_view,
    )



urlpatterns = [
    path("", home_view, name="home"),
    path("detail/<sales_id>", detail_view),
    path("list/", list_view),
    path("buscar/<nombre_usuario>", search_view),
    path("crear/<nombre_usuario>/<codigo>", create_view),

    path("buscar-con-formulario/", search_with_form_view, name="buscar-con-formulario"),
    path("crear-con-formulario/", create_with_form_view, name="crear-con-formulario"),
    path("crear-codigo-formulario/", create_codigo_with_form_view, name="crear-codigo-formulario"),
    path("detail-codigo/<codigo_id>", detail_codigo_view),
    path("crear-usuario/", user_creation_view, name="crear-usuario"),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),


    


    

]
