# Cadenas
# Las cadenas son inmutables

comando = "upper"
print(id(comando))

otro_comando = comando  # Asigno como valor a otra variable
print(id(otro_comando))

comando = comando + "()"
print(id(comando))
print(comando)