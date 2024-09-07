from dataclasses import dataclass


@dataclass
class Ciudad:
    nombre: str
    poblacion: int


@dataclass
class Persona:
    nombre: str
    edad: int
    ciudad_origen: Ciudad


@dataclass
class TarjetaCredito:
    titular: Persona
    numero: str
    vencimiento: str
    codigo: str


mendoza = Ciudad("Ciudad de Mendoza", 2_000_000)
cordoba = Ciudad(nombre="Ciudad de Córdoba", poblacion=2_050_000)
p1 = Persona(nombre="Lucía", edad=20, ciudad_origen=mendoza)
p2 = Persona(nombre="Juan", edad=25, ciudad_origen=cordoba)

print(p1.nombre)
print(p1.ciudad_origen.nombre)
print(p1.ciudad_origen.poblacion)
print(p1)

tarjeta1 = TarjetaCredito(p1, "12121", "12/26", "007")
tarjeta2 = TarjetaCredito(p2, "87878", "12/28", "807")
print(tarjeta1)
