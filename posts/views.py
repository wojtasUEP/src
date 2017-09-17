from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def posts_create(request):
    return HttpResponse("<h1>CREATE</h1>")

def posts_detail(request): #retrive
    return HttpResponse("<h1>DETAIL</h1>")

def posts_list(request): #list items
    return HttpResponse("<h1>LIST</h1>")

def posts_update(request):
    return HttpResponse("<h1>UPDATE</h1>")

def posts_delete(request):
    return HttpResponse("<h1>DELETE</h1>")