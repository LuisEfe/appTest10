from django.shortcuts import render
from django.http import HttpResponse

def index (request):
        return HttpResponse ("Hi Lushiiiii")

def hi (request):
        return HttpResponse ("<< This is another message >>")

def list_Clients (request):
        return HttpResponse ("<< Here you must list the clientes in DB >>")

# Create your views here.
