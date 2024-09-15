class Estudiante:
    nombre_escuela: str | None = None

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self, mensaje: str) -> None:  # método de instancia
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años. {mensaje}")

    @staticmethod
    def info():  # método estático
        print("Es un estudiante de esta escuela")

    # def cambiar_nombre_escuela(self):
    #     Estudiante.nombre_escuela = "Colegio Nacional"

    @classmethod
    def cambiar_nombre_escuela(cls, nuevo_valor: str) -> None:  # método de clase
        cls.nombre_escuela = nuevo_valor


instancia = Estudiante("Teresita", 6)
instancia.saludar("Me gusta programar en Python.")
instancia.info()
Estudiante.info()
Estudiante.cambiar_nombre_escuela("Colegio Nacional")
print(Estudiante.nombre_escuela)
