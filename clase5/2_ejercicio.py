"""
- Crear una clase Persona
  que contenga los atributos:
    - nombre: str
    - edad: str

- Crear 3 instancias de Persona
- Mostrar por pantalla un mensaje elaborado
"""


class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad


p1 = Persona("Lucía", 11)
p2 = Persona("Julián", 5)
p3 = Persona("Teresa", 2)

# print(f"Mi nombre es {p1.nombre}, y tengo {p1.edad} años de edad.")
# print(f"Mi nombre es {p2.nombre}, y tengo {p2.edad} años de edad.")
# print(f"Mi nombre es {p3.nombre}, y tengo {p3.edad} años de edad.")
lista_de_objetos = [p1, p2, p3]

for persona in lista_de_objetos:
    print(f"Mi nombre es {persona.nombre}, y tengo {persona.edad} años de edad.")
