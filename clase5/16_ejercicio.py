"""
✨ EJERCICIO ✨
Crear las siguientes clases:
    -DarBienvenida
        método: dar_bienvenida
    -Persona
        constructor:
            -nombre
            -dar_bienvenida()

Cuando cree una instancia de Persona, Python debe imprimir "Bienvenido {nombre}"
"""


class DarBienvenida:
    def dar_bienvenida(self, nombre: str):
        print(f"Bienvenido {nombre}")


class Persona(DarBienvenida):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.dar_bienvenida(nombre)


p = Persona("Isabella")
p.dar_bienvenida("otra persona")
