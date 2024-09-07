class Guitarra:
    def __init__(self, sonido: str):
        self.sonido = sonido

    def ejecutar(self):
        print(self.sonido)


class GuitarraElectrica(Guitarra):
    def distorsion(self):
        print("tran tran tran")


# guitarra = Guitarra("tan tan tan")
# guitarra.ejecutar()  # Imprime: "tan tan tan"

guitarra_electrica = GuitarraElectrica("tun tun tun")
guitarra_electrica.ejecutar()  # Imprime: "tun tun tun"
guitarra_electrica.distorsion()  # Imprime: "tran tran tran"
