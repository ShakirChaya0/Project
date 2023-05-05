sub_menu = "a"
if sub_menu == "a": 
  lista_nombres = []
  decision = "si"

  while decision == "si" or decision == "sí":
    nombre = input("Escriba el nombre de el local que desea crear: ")
    decision = input("¿Quiere seguir agregando locales? (Si o No):")
    decision.lower
    lista_nombres.append(nombre)


  lista_rubros = []
  bandera = True
  
  while bandera:
    for i in lista_nombres:
      rubros = input("Escriba el rubro de cada local: ")
      rubros.lower
      if rubros == "comida" or rubros == "indumetaria" or rubros == "perfumeria":
        lista_rubros.append(rubros)
      else:
        print("El rubro que ha elegido no existe, intentelo de nuevo")

  
  lista_ubicaciones = []

  for i in lista_nombres:
    ubicaciones = input("Escriba la ubicación de cada local: ")
    lista_ubicaciones[i] = ubicaciones














