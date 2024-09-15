class Empleado:
    def __init__(self, especialidad, seguro, salario) -> None:
        self.especialidad = especialidad
        self.seguro = seguro
        self.__salario = salario  # atributo privado

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario


class EmpleadoBonificado(Empleado):
    def __init__(self, especialidad, seguro, salario, salario_bonificado, bono) -> None:
        super().__init__(especialidad, seguro, salario)
        self.__salario = salario_bonificado
        self.bono = bono

    def __calcular_salario_total(self):
        return super().get_salario() + self.__salario + self.bono

    def get_salario(self):  # sobreescribiendo el método get_salario de la clase padre
        return self.__calcular_salario_total()


empleado = Empleado(
    especialidad="Desarrollador",
    seguro="Seguro de vida",
    salario=10000,
)
empleado_bonificado = EmpleadoBonificado(
    especialidad="Desarrollador Python",
    seguro="Seguro de vida",
    salario=10000,
    salario_bonificado=2000,
    bono=5000,
)

print(vars(empleado))
print(vars(empleado_bonificado))

# print(empleado.__salario)  # no funciona porque es un atributo privado
print(empleado.get_salario())
# empleado.__salario = 12000  # crea otro atributo __salario diferente al atributo privado de la clase
empleado.set_salario(12000)

print(empleado_bonificado.get_salario())
