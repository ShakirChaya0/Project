import sys 
import getpass

def reinicio():
  sys.exit(0)
def separador():
  print(70 * "-")

nombre_usuario = "1"
clave_contraseña = "1"
intentos = 0

inicio_usuario = input("Ingrese el Usuario: ")
inicio_contraseña = getpass.getpass("Ingrese la contraseña: ")

while (inicio_usuario != nombre_usuario or inicio_contraseña != clave_contraseña) or (len(inicio_usuario) > 100 or len(inicio_contraseña) > 8):
  intentos += 1
  if intentos == 3:
    reinicio()
  separador()
  print("El usuario o la contraseña son inválidos")
  inicio_usuario = input("Ingrese el Usuario: ")
  inicio_contraseña = getpass.getpass("Ingrese la contraseña: ")

menu_principal = {
   "1" : "Gestion de locales", 
   "2" : "Crear cuentas de dueños de locales",
   "3" : "Aprobar / Denegar solicitud de descuento",
   "4" : "Gestión de Novedades",
   "5" : "Reporte de utilización de descuentos",
   "0" : "Salir"
}

sub_menu = 0
inicio_menu_principal = 0
bandera = True

while bandera:
  inicio_menu_principal = 0
  sub_menu = 0
  while inicio_menu_principal != "1" and inicio_menu_principal != "2" and inicio_menu_principal != "3" and  inicio_menu_principal != "4" and inicio_menu_principal != "5" and inicio_menu_principal != "0":
    separador()
    if inicio_menu_principal != "1" and inicio_menu_principal != "2" and inicio_menu_principal != "3" and  inicio_menu_principal != "4" and inicio_menu_principal != "5" and inicio_menu_principal != "0" and inicio_menu_principal != 0:
      print("La opción que has elegido es incorrecta, intentelo de nuevo ingresando un numero del 0 al 5.")
    inicio_menu_principal = input(
"""---------------Menu principal---------------
      0. Salir
      1. Gestion de locales
      2. Crear cuentas de dueños de locales
      3. Aprobar / Denegar solicitud de descuento
      4. Gestión de Novedades
      5. Reporte de utilización de descuentos
Escoger la opción a la que desee acceder: """)
    if inicio_menu_principal == "0":
      reinicio()
    if inicio_menu_principal == "2" or inicio_menu_principal == "3" or inicio_menu_principal == "4" or inicio_menu_principal == "5":
      separador()
      print("Lo sentimos, esta sección esta en construcción...")
    if inicio_menu_principal == "1":
      while sub_menu != "a" and sub_menu != "b" and sub_menu != "c" and sub_menu != "d":
        if sub_menu != "a" and sub_menu != "b" and sub_menu != "c" and sub_menu != 0:
          separador()
          print("La opción que has elegido es incorrecta, intentelo de nuevo ingresando una de las letras dadas.")
        sub_menu = input(
"""---------------Gestión de locales---------------
      a) Crear locales
      b) Modificar local
      c) Eliminar local
      d) Volver
Escoger la opción a la que desee acceder: """)
        if sub_menu == "b" or sub_menu == "c":
          separador()
          print("Lo sentimos, esta sección esta en construcción...")
          bandera = False
        if sub_menu == "a":
          lista = []
          separador()
          bandera = False

if sub_menu == "a": 
  lista_nombres = []
  decision = "si"
  comida = 0
  indumentaria = 0 
  perfumería = 0

  while decision == "si" or decision == "sí":
    nombre = input("Escriba el nombre de el local que desea crear: ")
    decision = input("¿Quiere seguir agregando locales? (Si o No):")
    decision.lower
    lista_nombres.append(nombre)


  lista_rubros = []
  bandera = True
  
  separador()
  for i in lista_nombres:
    print("Los rubros disponibles son: Comida, Indumentaria y Perfumería")
    rubros = input("""Escriba el rubro de cada local: """)
    rubros.lower
    if rubros == "comida" or rubros == "indumentaria" or rubros == "perfumeria" or rubros == "perfumería":
      lista_rubros.append(rubros)
    else:
      separador()
      print("El rubro que ha elegido no existe, intentelo de nuevo")
      rubros = input("Escriba el rubro de cada local respectivamente: ")
      rubros.lower
      lista_rubros.append(rubros)

  lista_ubicaciones = []
  separador()
  for i in lista_nombres:
    ubicaciones = input("Escriba la ubicación de cada local respectivamente: ")
    lista_ubicaciones.append(ubicaciones)

  separador()

  for rubro in lista_rubros:
    if rubro == "comida":
      comida += 1
    elif rubro == "indumentaria":
      indumentaria += 1
    elif rubro == "perfumería" or rubro == "perfumeria":
      perfumería += 1


  if comida > indumentaria and comida > perfumería:
    print(f"El rubro con más locales es comida, con {comida} locales")
  elif indumentaria > comida and indumentaria > perfumería:
    print(f"El rubro con más locales es indumentaria, con {indumentaria} locales")
  elif perfumería > indumentaria and perfumería > comida:
    print(f"El rubro con más locales es perfumería, con {perfumería} locales")


  if comida < indumentaria and comida < perfumería:
    print(f"El rubro con menos locales es comida, con {comida} locales")
  elif indumentaria < comida and indumentaria < perfumería:
    print(f"El rubro con menos locales es indumentaria, con {indumentaria} locales")
  elif perfumería < indumentaria and perfumería < comida:
    print(f"El rubro con menos locales es perfumería, con {perfumería} locales")
    
  if comida == indumentaria and indumentaria == perfumería:
    print("La cantidad de locales con cada rubro es igual")




