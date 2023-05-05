import getpass
import os

nombre_usuario = "1"
clave_usuario = "1"
eleccion = None
decision = None
perfumeria = 0
comida = 0
indumentaria = 0

def mostrar_menu():
  global eleccion
  
  if eleccion != "1" and eleccion != "4" and eleccion != "0":
    print(
  """---------------Menu principal---------------
      0. Salir
      1. Gestion de locales
      2. Crear cuentas de dueños de locales
      3. Aprobar / Denegar solicitud de descuento
      4. Gestión de Novedades
      5. Reporte de utilización de descuentos""")
    
  elif eleccion == "1":
    print(
  """---------------Gestión de locales---------------
        a) Crear locales
        b) Modificar local
        c) Eliminar local
        d) Volver""")
    
  elif eleccion == "4":
    print(
  """---------------Gestión de Novedades---------------
        a) Crear novedades
        b) Modificar novedad
        c) Eliminar novedad
        d) Ver reporte de novedades
        e) Volver""")

def separador():
  print(70 * "-")

def pedirusuario():
  global eleccion
  contador = 0
  usuario = None
  contraseña = None
  
  while (usuario != nombre_usuario or contraseña != clave_usuario) and contador < 3:
   usuario = input("Escriba su usuario: ")
   contraseña = getpass.getpass("Escriba su contraseña: ")
   contador = contador + 1
   
   os.system("cls")
   
   if usuario == nombre_usuario and contraseña == clave_usuario:
      print("Hola, has ingresado correctamente")
      
   elif contador < 3:
      print("Su usuario o contraseño son incorrectos, intentelo de nuevo")
      separador()
      
   else:
      print("Su numero de intentos ha finalizado")
      eleccion = "1"

def gestion_de_locales():
  global eleccion
  global decision

  if eleccion == "1":
    
    while decision != "a" and decision != "b" and decision != "c" and decision != "d":
      mostrar_menu()
      decision = input("Escoger la opción a la que desee acceder: ")
      
      os.system("cls")
      
      if decision != "a" and decision != "b" and decision != "c" and decision != "d":
        separador()
        print("La opción que has elegido es incorrecta, intentelo de nuevo ingresando una de las letras dadas.")
        
      elif decision == "a":
        Crear_Locales()
        decision = None
        
      elif decision == "b" or decision == "c":
        separador()
        print("Lo sentimos esta sección esta en construcción, quiere intentar ingresar a otra sección.")
        decision = None
        
      elif decision == "d":
        eleccion = None
        decision = None

def gestion_de_novedades():
  global eleccion
  global decision

  if eleccion == "4":
    
    while decision != "a" and decision != "b" and decision != "c" and decision != "d" and eleccion != "e":
      mostrar_menu()
      decision = input("Escoger la opción a la que desee acceder: ")
      
      os.system("cls")

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

def Crear_Locales():
  intentos = 0
  global perfumeria
  global comida
  global indumentaria
  cant_locales = None 
  
  while cant_locales != "1" and cant_locales != "2" and cant_locales != "3" and cant_locales != "4" and cant_locales != "5":
    
    os.system("cls")
    
    cant_locales = input(
        "Ingrese nuevamente la cantidad de locales a ingresar(no mas de cinco): ")
    if cant_locales != "1" and cant_locales != "2" and cant_locales != "3" and cant_locales != "4" and cant_locales != "5":
      
      print("Usted a seleccionado una cantidad erronea, intentelo de nuevo")
    
    
  cant_locales = int(cant_locales)

  while ((intentos < cant_locales) and (intentos < 5)):
    
    separador()
    
    nombre = input("Ingrese el nombre de el local: ")
    Ubicacion = input("Ingrese la ubicación del local: ")
    rubro = input("Ingrese el tipo de rubro del local (perfumeria, comida o indumentaria): ")
    rubro = rubro.lower()
    
    if (rubro == "perfumeria") or (rubro == "perfumería"):
      perfumeria += 1
      intentos += 1
      
    elif (rubro == "indumentaria"):
      indumentaria += 1
      intentos += 1
      
    elif (rubro == "comida"):
      comida += 1
      intentos += 1
      
    elif (rubro != "perfumeria", "perfumería", "indumentaria", "comida"):
      print("Usted no ingreso los datos correctamente porfavor intentelo otra vez (Tenga en cuenta las mayusculas y los acentos)")
      
    if ((indumentaria > comida) and (indumentaria > perfumeria)):
      local_mayor = (f"El rubro con la mayor cantidad de locales es: indumentaria, con una cantidad de: {indumentaria} local/es""")
      
    elif ((comida > indumentaria) and (comida > perfumeria)):
      local_mayor = (f"El rubro con la mayor cantidad de locales es: comida, con una cantidad de: {comida} local/es")
    
    elif ((perfumeria > indumentaria) and (perfumeria > comida)):
      local_mayor = (f"El rubro con la mayor cantidad de locales es: perfumeria, con una cantidad de: {perfumeria} local/es")
      
    elif comida == indumentaria:
      local_mayor = (f"Los rubros con la mayor cantidad de locales son: comida e indumentaria, con una cantidad de: {comida} local/es")
      
    elif perfumeria == indumentaria:
      local_mayor = (f"Los rubros con la mayor cantidad de locales son: perfumeria e indumentaria, con una cantidad de: {indumentaria} local/es")
      
    elif comida == perfumeria:
      local_mayor = (f"Los rubros con la mayor cantidad de locales son: comida y perfumeria, con una cantidad de: {comida} local/es")
      
    else:
      local_mayor = (f"Todos los rubros tienen la misma cantidad de locales, con una cantidad de: {comida} local/es")
      
    if ((indumentaria < comida) and (indumentaria < perfumeria)):
      local_menor = (f"El rubro con la menor cantidad de locales es: indumentaria, con una cantidad de: {indumentaria} local/es")
      
    elif ((comida < indumentaria) and (comida < perfumeria)):
      local_menor = (f"El rubro con la menor cantidad de locales es: comida, con una cantidad de: {comida} local/es")
    
    elif ((perfumeria < indumentaria) and (perfumeria < comida)):
      local_menor = (f"El rubro con la menor cantidad de locales es: perfumeria, con una cantidad de: {perfumeria} local/es")
      
    elif comida == indumentaria:
      local_menor = (f"Los rubros con la menor cantidad de locales son: comida e indumentaria, con una cantidad de: {comida} local/es")
      
    elif perfumeria == indumentaria:
      local_menor = (f"Los rubros con la menor cantidad de locales son: perfumeria e indumentaria, con una cantidad de: {indumentaria} local/es")
      
    elif comida == perfumeria:
      local_menor = (f"Los rubros con la menor cantidad de locales son: comida y perfumeria, con una cantidad de: {comida} local/es")
      
    else:
      local_menor = (f"Todos los rubros tienen la misma cantidad de locales, con una cantidad de: {comida} local/es")
      
  os.system("cls")
  separador()
  print(local_mayor)
  print(local_menor)

pedirusuario()

while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5" and eleccion != "0":
  separador()
  mostrar_menu()
  eleccion = input("Escoger la opción a la que desee acceder: ")
  
  os.system("cls")
  
  if eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5" and eleccion != "0":
    print("La opción que has elegido es incorrecta, intentelo de nuevo ingresando un numero del 0 al 5.")
    
  elif eleccion == "0":
    print("Saliendo del programa...")
    
  elif eleccion == "1":
    gestion_de_locales()
    
  elif eleccion == "2" or eleccion == "3" or eleccion == "5":
    separador()
    print("Lo sentimos, esta sección esta en construcción, quiere intentar ingresar a otra sección?")
    eleccion = None
    
  elif eleccion == "4":
    gestion_de_novedades()
