"""
✨ EJERCICIO ✨
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

A partir del código anterior agregar el atributo apellido
- Crear un método de instancia: nombre_completo()
El método mostrará primero el apellido en mayúsculas, luego una coma,
un espacio y el primer caracter del nombre en mayúsculas y el resto en minúsculas
"""


class Persona:
    def __init__(self, nombre: str, apellido: str, edad: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self) -> str:
        return f"{self.apellido.upper()}, {self.nombre.capitalize()}"


persona_1 = Persona("Juan", "Pérez", 25)
persona_2 = Persona("Pedro", "Rodriguez", 40)
persona_3 = Persona("Maria", "Gonzalez", 35)

print(persona_1.nombre_completo())
print(persona_2.nombre_completo())
print(persona_3.nombre_completo())
