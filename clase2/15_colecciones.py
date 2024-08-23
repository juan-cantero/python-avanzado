usuarios = [
    {
        "nombre": "Juan",
        "nacionalidades": ["española", "francesa", "italiana"],
    },
    {
        "nombre": "Jorge",
        "nacionalidades": ["española"],
    },
]

juan = usuarios[0]["nombre"]
print(juan)

buscar = "Jorge"
for usuario in usuarios:
    if usuario["nombre"] == buscar:
        print(f"{buscar} encontrado")
        break
else:
    print(f"{buscar} no encontrado")