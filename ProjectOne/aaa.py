lista_nombres = []
decision = "si"

while decision == "si" or decision == "sí":
  nombre = input("Escriba el nombre de el local que desea crear: ")
  decision = input("¿Quiere seguir agregando locales? (Si o No):")
  decision.lower
  lista_nombres.append(nombre)


lista_rubros = []

for i in lista_nombres:
  rubros = input("Escriba el rubro de cada local: ")
  lista_rubros.append(rubros)

lista_ubicaciones = []

for i in lista_nombres:
  ubicaciones = input("Escriba la ubicación de cada local: ")
  lista_ubicaciones.append(ubicaciones)













