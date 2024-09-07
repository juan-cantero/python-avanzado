class Ciudad:
    def __init__(self, nombre: str, poblacion: int) -> None:  # método constructor
        self.nombre = nombre  # atributo o variable de instancia
        self.poblacion = poblacion  # atributo o variable de instancia


mendoza = Ciudad("Ciudad de Mendoza", poblacion=2_000_000)  # instancia u objeto de la clase Ciudad
cordoba = Ciudad("Ciudad de Córdoba", poblacion=2_050_000)  # instancia u objeto de la clase Ciudad

print(mendoza.nombre, mendoza.poblacion)
print(cordoba.nombre, cordoba.poblacion)
