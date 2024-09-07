class Ruedas:
    def __init__(self, cantidad: int):
        self.cantidad = cantidad


class Auto:
    def __init__(self, nombre: str, ruedas: Ruedas) -> None:
        self.nombre = nombre
        self.ruedas = ruedas


ruedas_para_mi_auto = Ruedas(cantidad=4)
mi_auto = Auto("Fiat", ruedas_para_mi_auto)

print(mi_auto.nombre, mi_auto.ruedas.cantidad)
