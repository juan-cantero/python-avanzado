class Vehiculo:
    def arrancar(self):
        print("El vehículo ha arrancado")


class Auto(Vehiculo):
    def tocar_bocina(self):
        print("¡Piiiii!")


class MovimientosMarianosMixin:
    def virar_estribor(self):
        print("Virando a estribor")

    def virar_babor(self):
        print("Virando a babor")


class Lancha(Vehiculo, MovimientosMarianosMixin):
    pass


vehiculo = Vehiculo()
vehiculo.arrancar()
auto = Auto()
auto.arrancar()
auto.tocar_bocina()
lancha = Lancha()
lancha.arrancar()
lancha.virar_babor()
lancha.virar_estribor()
