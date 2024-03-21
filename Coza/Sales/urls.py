from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def vista2(w2):
    return HttpResponse("<h1>Sales 2024</h1>")

urlpatterns = [
    path("", vista2)
    
]
