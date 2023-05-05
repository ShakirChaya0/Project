import getpass
import os

nombre_usuario = "1"
clave_usuario = "1"
eleccion = None
decision = None
perfumeria = 0
comida = 0
indumentaria = 0 


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
    mostrar_menu_principal()
    eleccion = input("Escoger la opción a la que desee acceder: ")
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
      decision = input("Escoger la opción a la que desee acceder: ")
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
        menu_principal()

def gestion_de_novedades():
  global eleccion
  global decision

  if eleccion == "4":
    while decision != "a" and decision != "b" and decision != "c" and decision != "d" and eleccion != "e" and eleccion == "4":
      decision = input("Escoger la opción a la que desee acceder: ")
      
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

def Crear_Locales():
   Intentos = 0
   global perfumeria  
   global comida 
   global indumentaria 
   
   Cant_Locales = input ("Ingrese la cantidad de locales a ingresar(no mas de cinco): ")
   while Cant_Locales != "1" and Cant_Locales != "2" and Cant_Locales != "3" and Cant_Locales != "4" and Cant_Locales != "5":
      print("Usted a seleccionado una cantidad erronea, intentelo de nuevo")
      Cant_Locales = input("Ingrese nuevamente la cantidad de locales a ingresar(no mas de cinco): ")
   Cant_Locales = int (Cant_Locales)

   while((Intentos < Cant_Locales) and (Intentos < 5)):
      #agregar nombre local y ubi
      Rubro = input("Ingrese el tipo de rubro del local (perfumeria, comida o indumentaria): ")
      Rubro = Rubro.lower()
      if(Rubro == "perfumeria") or (Rubro == "perfumería"):
         perfumeria += 1
         Intentos += 1
      elif(Rubro == "indumentaria"):
         indumentaria += 1
         Intentos += 1
      elif(Rubro == "comida"):
         comida += 1
         Intentos += 1
      elif(Rubro != "perfumeria", "perfumería","indumentaria","comida"):
         print("Usted no ingreso los datos correctamente porfavor intentelo otra vez (Tenga en cuenta las mayusculas y los acentos)")

   if((indumentaria >= comida) and (indumentaria >= perfumeria)):
      Local_Mayor = "El rubro con la mayor cantidad de locales es: indumentaria, con una cantidad de: ",indumentaria, " locales"
   elif((comida >= indumentaria) and (comida >= perfumeria)):
      Local_Mayor = "El rubro con la mayor cantidad de locales es: comida, con una cantidad de: ",comida, " locales"
   else:
      Local_Mayor = "El rubro con la mayor cantidad de locales es: perfumeria, con una cantidad de: ",perfumeria, " locales"
   
   if((indumentaria <= comida) and (indumentaria <= perfumeria)):
      Local_Menor = "El rubro con la menor cantidad de locales es: indumentaria, con una cantidad de: ",indumentaria," locales"
   elif((comida <= indumentaria) and (comida <= perfumeria)):
      Local_Menor = "El rubro con la menor cantidad de locales es: comida, con una cantidad de: ",comida, " locales"
   else:
      Local_Menor = "El rubro con la menor cantidad de locales es: perfumeria, con una cantidad de: ",perfumeria, " locales"

   print(Local_Mayor)
   print(Local_Menor)



pedirusuario()
menu_principal()
gestion_de_locales()
gestion_de_novedades()