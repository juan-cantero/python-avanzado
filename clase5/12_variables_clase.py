class Usuario:
    sistema = "Django"  # variable de clase

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password


admin = Usuario("admin", "admin123")
user = Usuario("user", "aquiestoy")

# print(admin.sistema)  # Django
# print(user.sistema)  # Django

# print(admin.__dict__)
# print(vars(admin))
# print()
# print(user.__dict__)
# print(vars(user))

# admin.sistema = "Flask"  # crea una variable de instancia -> no es lo deseado
Usuario.sistema = "Flask"  # modifica la variable de clase
print(admin.sistema)
print(user.sistema)
print(vars(admin))
print(vars(user))
