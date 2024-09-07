class Especie:
    def __init__(self, nombre: str):
        self.nombre = nombre


class Animal:
    def __init__(self, especie: Especie, nombre: str, sonido: str) -> None:
        self.especie = especie
        self.nombre = nombre
        self.sonido = sonido

    def hacer_sonido(self) -> None:  # método de instancia
        print(f"{self.nombre} hace '{self.sonido}'")


canis = Especie("Canis")
felis = Especie("Felis")

animal_1 = Animal(canis, "Fido", "Guau")
animal_2 = Animal(felis, "Garfield", "Miau")

animal_1.hacer_sonido()
animal_2.hacer_sonido()
