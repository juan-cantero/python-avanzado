"""
Crear una función que tenga como parámetros:
  - nombre
  - fecha de nacimiento (opcional)

Pedir al usuario que ingrese los datos y mostrarlos
Si no ingresa fecha de nacimiento, mostrar el mensaje "no ingresó fecha de nacimiento"

Código:
nombre = input("Ingrese su nombre: ")
fecha_nacimiento = input("Ingrese su fecha de nacimiento (opcional): ")
if fecha_nacimiento == "":
    print("No ingresó fecha de nacimiento")
else:
    print("Nombre:", nombre)
    print("Fecha de nacimiento:", fecha_nacimiento)
"""


def ingresar_datos() -> tuple[str, str]:
    """Pide al usuario que ingrese su nombre y fecha de nacimiento (opcional)
    y los devuelve como una tupla."""
    nombre = input("Ingrese su nombre: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (opcional): ")
    return nombre, fecha_nacimiento


def mostrar_datos(nombre: str, fecha_nacimiento=None) -> None:
    """Muestra el nombre y la fecha de nacimiento (si se proporciona) del usuario."""
    print("Nombre:", nombre)
    if fecha_nacimiento:
        print("Fecha de nacimiento:", fecha_nacimiento)
    else:
        print("No ingresó fecha de nacimiento")


def main():
    """Función principal que llama a las funciones ingresar_datos y mostrar_datos."""
    nombre, fecha_nacimiento = ingresar_datos()
    mostrar_datos(nombre, fecha_nacimiento)


main()
