import getpass

nombre_usuario = "1"
clave_usuario = "1"
eleccion = None
decision = None

def separador():
  print(70 * "-")

def pedirusuario():
  global eleccion
  Contador = 0
  Usuario = None
  Contraseña = None
  while ((Usuario != nombre_usuario) or (Contraseña != clave_usuario)) and Contador < 3: 
   Usuario = input("Escriba su usuario: ")
   Contraseña = getpass.getpass("Escriba su contraseña: ")
   Contador = Contador + 1
   if Usuario == nombre_usuario and Contraseña == clave_usuario:
      print ("Hola, has ingresado correctamente")
   elif Contador < 3:
      print ("Compruebe si su Usuario o Contraseña estan correctos. Vuelva a intentarlo")
   else:
      print("Su numero de intentos ha finalizado")
      eleccion = "1"

def menu_principal():
  global eleccion
  
  while eleccion != "1" and eleccion != "2" and eleccion != "3" and  eleccion != "4" and eleccion != "5" and eleccion != "0":
    separador()
    eleccion = input(
"""---------------Menu principal---------------
      0. Salir
      1. Gestion de locales
      2. Crear cuentas de dueños de locales
      3. Aprobar / Denegar solicitud de descuento
      4. Gestión de Novedades
      5. Reporte de utilización de descuentos
Escoger la opción a la que desee acceder: """)
    if eleccion != "1" and eleccion != "2" and eleccion != "3" and  eleccion != "4" and eleccion != "5" and eleccion != "0":
      print("La opción que has elegido es incorrecta, intentelo de nuevo ingresando un numero del 0 al 5.")
    elif eleccion == "2" or eleccion == "3" or eleccion == "5":
      separador()
      print("Lo sentimos, esta sección esta en construcción, quiere intentar ingresar a otra sección?")
      eleccion = None
    elif eleccion == "0":
      print("Saliendo del programa...")
    elif eleccion == "1":
      gestion_de_locales()
    elif eleccion == "4":
      gestion_de_novedades()

def gestion_de_locales():
  global eleccion
  global decision

  if eleccion == "1":
    while decision != "a" and decision != "b" and decision != "c" and decision != "d" and eleccion == "1":
      decision = input(
  """---------------Gestión de locales---------------
        a) Crear locales
        b) Modificar local
        c) Eliminar local
        d) Volver
  Escoger la opción a la que desee acceder: """)
      
      if decision != "a" and decision != "b" and decision != "c" and decision != "d":
        separador()
        print("La opción que has elegido es incorrecta, intentelo de nuevo ingresando una de las letras dadas.")
      elif decision == "a" or decision == "b" or decision == "c":
        separador()
        print("Lo sentimos esta sección esta en construcción, quiere intentar ingresar a otra sección.")
        decision = None
      elif decision == "d":
        eleccion = None
        decision = None
        menu_principal()

def gestion_de_novedades():
  global eleccion
  global decision

  if eleccion == "4":
    while decision != "a" and decision != "b" and decision != "c" and decision != "d" and eleccion != "e" and eleccion == "4":
      decision = input(
  """---------------Gestión de Novedades---------------
        a) Crear novedades
        b) Modificar novedad
        c) Eliminar novedad
        d) Ver reporte de novedades
        e) Volver
  Escoger la opción a la que desee acceder: """)
      
      if decision != "a" and decision != "b" and decision != "c" and decision != "d" and decision != "e":
        separador()
        print("La opción que has elegido es incorrecta, intentelo de nuevo ingresando una de las letras dadas.")
      elif decision == "a" or decision == "b" or decision == "c" or decision == "d":
        separador()
        print("Lo sentimos esta sección esta en construcción, quiere intentar ingresar a otra sección.")
        decision = None
      elif decision == "e":
        eleccion = None
        decision = None
        menu_principal()



pedirusuario()
menu_principal()
gestion_de_locales()
gestion_de_novedades()

