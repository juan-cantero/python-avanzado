"""
✨ EJERCICIO ✨
Agregar a Animal el método de instancia: andar()
andar() recibe un entero, son los pasos que puede dar el animal
Cuando se invoque andar(), se mostrará por pantalla el nombre del animal,
el nombre de la especie y cuántos pasos anduvo
Si no se agregan 'pasos', se entenderá que el animal no dio pasos.
"""


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

    def andar(self, pasos=0) -> None:
        if pasos > 0:
            m = f"El animal {self.especie.nombre} llamado '{self.nombre}' anduvo {pasos} pasos."
        elif pasos == 0:
            m = f"El animal {self.especie.nombre} llamado '{self.nombre}' no anduvo."
        else:
            m = "Hay un problema con los pasos ingresados."
        print(m)


canis = Especie("Canis")
felis = Especie("Felis")

animal_1 = Animal(canis, "Fido", "Guau")
animal_2 = Animal(felis, "Garfield", "Miau")

animal_1.andar(10)
animal_2.andar()
animal_2.andar(-12)
