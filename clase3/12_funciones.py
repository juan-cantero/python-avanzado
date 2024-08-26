def saludar(saludo):
    return saludo


def saludar_con_mayusculas(saludo: str) -> str:
    return saludo.upper()


saludo = saludar("hola!")
print(saludo)

saludo_con_mayusculas = saludar_con_mayusculas("chau")
print(saludo_con_mayusculas)
