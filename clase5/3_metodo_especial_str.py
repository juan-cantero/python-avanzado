class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Mi nombre es {self.nombre}, y tengo {self.edad} años de edad."


p1 = Persona("Lucía", 11)
p2 = Persona("Julián", 5)
p3 = Persona("Teresa", 2)

print(p1)
print(p2)
print(p3)

# return_de_str = p1.__str__()
# print(return_de_str)
