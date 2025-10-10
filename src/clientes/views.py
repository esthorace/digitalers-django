from django.shortcuts import render

from .models import Cliente, Pais


def index(request):
    return render(request, "clientes/index.html")


def pais_list(request):
    paises = Pais.objects.all()
    return render(request, "clientes/pais_list.html", {"paises": paises})


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/cliente_list.html", {"clientes": clientes})
