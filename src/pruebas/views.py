from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render


def saludar(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hola desde Django!")


def saludar_con_etiqueta(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1> Este es el título de la página </h1>")


def saludar_con_parametros(
    request: HttpRequest, nombre: str, apellido: str
) -> HttpResponse:
    nombre_completo = f"{apellido.upper()}, {nombre.capitalize()}"
    return HttpResponse(f"<p>Hola <strong>{nombre_completo}</strong></p>")


def mi_json(request: HttpRequest) -> JsonResponse:
    usuarios: list[dict] = [
        {"nombre": "juan", "email": "juan@example.com"},
        {"nombre": "romina", "email": "romina@example.com"},
        {"nombre": "luli", "email": "luli@example.com"},
    ]
    return JsonResponse(usuarios, safe=False)


def index(request: HttpRequest) -> HttpResponse:
    from datetime import datetime

    año_actual = datetime.now().year
    contexto = {"año": año_actual}
    return render(request, "pruebas/index.html", contexto)
