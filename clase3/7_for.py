herramientas = [
    "Destornillador",
    "Llave inglesa",
    "Martillo",
    "Cinta métrica",
    "Nivel de burbuja",
]

# Quiero usar un martillo
for herramienta in herramientas:
    if herramienta != "Martillo":
        print(f"No quiero usar la herramienta {herramienta}. Necesito un martillo.")
        respuesta = input("¿Quieres continuar buscando? (s/n): ")
        if respuesta.lower() in ("s", "si", "sí"):
            continue
        elif respuesta.lower() in ("n", "no"):
            print("Entendido. No seguiré buscando.")
            break
        else:
            print("Respuesta no válida. Continuando la búsqueda.")
    else:
        print("¡Encontré un martillo! Ahora puedo usarlo.")
        break
