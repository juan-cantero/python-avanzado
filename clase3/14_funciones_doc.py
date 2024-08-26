def saludar(usuario: str) -> str:
    """
    parametro: nombre del usuario
    retorno: saludo personalizado para el usuario
    """
    mensaje = f"Hola, {usuario}! Bienvenido a nuestro servicio de atención al cliente."
    return mensaje


# Ejemplo de uso de la función
nombre_usuario = input("¿Cuál es tu nombre? ")
saludo = saludar(nombre_usuario)
print(saludo)

# Imprimir la documentación de la función
print(saludar.__doc__)
