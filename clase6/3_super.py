class Empleado:
    def __init__(self, especialidad, seguro, salario) -> None:
        self.especialidad = especialidad
        self.seguro = seguro
        self.salario = salario

    def enviar_email(self):
        print("Enviando email...")


class EmpleadoBonificado(Empleado):
    def __init__(self, especialidad, seguro, salario, bono) -> None:
        super().__init__(especialidad, seguro, salario)
        self.bono = bono

    def enviar_email(self):
        print("Enviando email desde la clase hija...")
        super().enviar_email()


empleado = Empleado("Desarrollador", "Seguro de vida", 10000)
empleado_bonificado = EmpleadoBonificado("Desarrollador Python", "Seguro de vida", 10000, 5000)

print(vars(empleado))
print(vars(empleado_bonificado))

empleado.enviar_email()
empleado_bonificado.enviar_email()
