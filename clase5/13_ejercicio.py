"""
✨ EJERCICIO ✨
A partir de la siguiente clase

class Usuario:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

Crear una variable de clase que consista en una lista de instancias de la misma clase Usuario
(dentro del método constructor llamar a la variable de clase 
y con append agregar el mismo objeto: self)
"""
from typing import Self

class Usuario:

    usuarios: list[Self] = []

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        Usuario.usuarios.append(self)

    def __str__(self) -> str:
        return self.username
    
    def __repr__(self) -> str:
        return f"Usuario(username='{self.username}', password='{self.password}')"
    
    def mostrar_usuarios(self):
        for usuario in Usuario.usuarios:
            print(usuario.username, usuario.password)

admin = Usuario("admin", "admin123")
user = Usuario("user", "aquiestoy")

# Usuario.usuarios.append(admin)
# Usuario.usuarios.append(user)

print(Usuario.usuarios)

# for usuario in Usuario.usuarios:
#     print(usuario.username, usuario.password)

admin.mostrar_usuarios()