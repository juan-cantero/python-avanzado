"""
✨ EJERCICIO ✨
Crear las siguientes clases con dataclass
    - Especie
        nombre: str
    - Animal
        especie: Especie
        nombre: str
        sonido: str
"""

from dataclasses import dataclass


@dataclass
class Especie:
    nombre: str


@dataclass
class Animal:
    especie: Especie
    nombre: str
    sonido: str


especie = Especie(nombre="canis Lupus")
animal = Animal(especie=especie, nombre="Lobo", sonido="Aullido")

print(animal.especie.nombre, animal.nombre)
