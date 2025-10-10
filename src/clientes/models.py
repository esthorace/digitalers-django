from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Paises"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
