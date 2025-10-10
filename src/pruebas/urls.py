from django.urls import path

from pruebas.views import (
    index,
    listar_notas,
    mi_json,
    nombres,
    saludar,
    saludar_con_etiqueta,
    saludar_con_parametros,
    tirar_dado,
)

app_name = "pruebas"

urlpatterns = [
    path("", index, name="index"),
    path("saludar/", saludar, name="saludar"),
    path("saludar2/", saludar_con_etiqueta, name="saludar_con_etiqueta"),
    path(
        "saludar3/<str:nombre>/<str:apellido>",
        saludar_con_parametros,
        name="saludar_con_parametros",
    ),
    path("json/", mi_json, name="mi_json"),
    path("notas/list/", listar_notas, name="listar_notas"),
    path("nombres/", nombres, name="nombres"),
    path("dados/", tirar_dado, name="tirar_dado"),
]
