import pandas

datos = pandas.read_csv("dataset_turnos_detalle.csv")
# print(datos)
# print(datos.head(3))
# print(datos.tail(2))
# print(datos["sede"])
# print(datos["sede"].value_counts())
print(datos["servicio"].value_counts())
