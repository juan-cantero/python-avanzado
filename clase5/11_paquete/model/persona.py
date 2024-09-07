class Persona:
    def __init__(self, nombre: str, apellido: str, edad: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self) -> str:
        return f"{self.apellido.upper()}, {self.nombre.capitalize()}"


if __name__ == "__main__":
    print("Bienvenido a la clase Persona")
