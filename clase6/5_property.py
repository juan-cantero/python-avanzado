class Empleado:
    def __init__(self, especialidad, seguro, salario) -> None:
        self.especialidad = especialidad
        self.seguro = seguro
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.getter
    def salario(self):
        if self.__salario == 0:
            return "No tiene salario asignado"
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor > 0:
            self.__salario = valor
        else:
            raise ValueError("El salario no puede ser negativo o 0")

    @salario.deleter
    def salario(self):
        print("Restableciendo a 0")
        self.__salario = 0

    def cambiar_salario_porcentaje(self, porcentaje: float) -> None:
        if isinstance(porcentaje, float | int):
            self.__salario += self.__salario * porcentaje / 100
        else:
            raise ValueError("Debes introducir un número")


empleado = Empleado(
    especialidad="Desarrollador",
    seguro="Seguro de vida",
    salario=1000,
)
# 1º parte
# print(empleado.salario)
# # empleado.set_salario(12000)
# empleado.salario = 12000
# print(empleado.salario)

# 2º parte
# print(empleado.salario)
# empleado.salario = 30000
# print(empleado.salario)
# print("deleter")
# del empleado.salario
# print(empleado.salario)

# 3º parte
print(empleado.salario)
empleado.cambiar_salario_porcentaje(100)
print(empleado.salario)
