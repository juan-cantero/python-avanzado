class Padre:
    def mensaje_padre(self):
        print("soy la clase Padre")


class Hijo(Padre):
    def mensaje_hijo(self):
        print("soy la clase Hijo")


a = Hijo()
a.mensaje_padre()
a.mensaje_hijo()
