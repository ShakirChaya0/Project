print("Ingrese los datos de los locales que desee crear (máximo tres)")
nombres = nombre1, nombre2, nombre3 = input("Ingrese los nombres separados por comas, por favor: ").split(",")

rubro1, rubro2, rubro3 = 0, 0, 0 

while (rubro1 != 1) and (rubro1 != 2) and (rubro1 != 3):
  rubro1 = input("""Ingrese el número según el rubro seleccionado:
        1. Comida
        2. Indumentaria
        3. Perfumería """)
  if rubro1 != 1 or rubro1 != 2 or rubro1 != 3:
    print("Rubro no válido")

  print("---------------------------------")
  

ubicaciones = ubi_1, ubi_2, ubi_3 = input("Ingrese las ubicaciones separadas por comas acorde al orden de su rubro: ").split(",")

comida = 0
indumentaria = 0
perfumería = 0

for rubro in rubros:
  if rubro == "comida":
        comida += 1
  elif rubro == "indumentaria":
        indumentaria += 1
  elif rubro == "perfumería":
        perfumería += 1
                        
if comida > 1:
  print(f"El rubro con más locales es comida, con {comida} locales")
elif indumentaria > 1:
  print(f"El rubro con más locales es comida, con {indumentaria} locales")
elif perfumería > 1:
  print(f"El rubro con más locales es comida, con {perfumería} locales") 