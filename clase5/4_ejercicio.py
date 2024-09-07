"""
✨ EJERCICIO

A partir del siguiente código, crear el método __str__ (método especial)

class Ciudad:
    def __init__(self, nombre: str, poblacion: int) -> None:
        self.nombre = nombre
        self.poblacion = poblacion

mendoza = Ciudad("Ciudad de Mendoza", 2_000_000)
cordoba = Ciudad(nombre="Ciudad de Córdoba", poblacion=2_050_000)
"""


class Ciudad:
    def __init__(self, nombre: str, poblacion: int) -> None:
        self.nombre = nombre
        self.poblacion = poblacion

    def __str__(self) -> str:
        linea1 = f"Ciudad: {self.nombre}\n"
        linea2 = f"Población: {self.poblacion}\n"
        return linea1 + linea2


mendoza = Ciudad("Ciudad de Mendoza", 2_000_000)
cordoba = Ciudad(nombre="Ciudad de Córdoba", poblacion=2_050_000)

print(mendoza)
print(cordoba)
