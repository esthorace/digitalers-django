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


def listar_notas(request):
    notas = [10, 8, 9, 4, 7]
    return render(request, "pruebas/notas.html", {"lista_notas": notas})


def nombres(request):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    datos = {
        "nombre": nombre,
        "apellido": apellido,
    }

    return render(request, "pruebas/nombres.html", context=datos)


def tirar_dado(request):
    from datetime import datetime
    from random import randint

    tiro_de_dado = randint(1, 6)

    if tiro_de_dado == 6:
        mensaje = f"Has tirado el 🎲 y has obtenido ¡{tiro_de_dado}! 🎉 Ganaste!!!"
    else:
        mensaje = f"Has tirado el 🎲 y has obtenido ¡{tiro_de_dado}! 🥶"
    datos = {
        "titulo": "Tiro de Dados",
        "mensaje": mensaje,
        "fecha": datetime.now().strftime("%H:%M:%S.%f"),
    }
    return render(request, "pruebas/dados.html", context=datos)
