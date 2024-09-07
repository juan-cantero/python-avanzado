class Bienvenida:
    def bienvenida(self):
        print("Bienvenida")


class Despedida:
    def despedida(self):
        print("Despedida")


class Saludos(Bienvenida, Despedida):
    pass


saludo = Saludos()
saludo.bienvenida()
saludo.despedida()
