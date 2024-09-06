archivo = open("nombre.txt", "w")  # modo write
archivo.write("Juan\n")
archivo.write("Julio\n")
archivo.close()

archivo = open("nombre.txt", "a", encoding="UTF-8")  # modo append
archivo.write("Pedro\n")
archivo.write("María\n")
archivo.close()

archivo = open("nombre.txt", "r", encoding="UTF-8")  # modo read
contenido = archivo.read()
print(contenido)
