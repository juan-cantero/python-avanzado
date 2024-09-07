class Motor:
    def encender(self):
        print("Motor encendido")

    def parar(self):
        print("Motor parado")


class Auto:
    def __init__(self) -> None:
        self.motor = Motor()  # 👉 Composición

    def encender_auto(self):
        self.motor.encender()

    def parar_auto(self):
        self.motor.parar()


mi_auto = Auto()
mi_auto.encender_auto()
mi_auto.parar_auto()
