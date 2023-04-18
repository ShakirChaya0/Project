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

inicio_menu_principal = 0

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
if inicio_menu_principal != "1":
  separador()
  print("Lo sentimos, esta sección esta en construcción...")
  
  
sub_menu = 0

if inicio_menu_principal == "1":
  while sub_menu != "a" and sub_menu != "b" and sub_menu != "c" and sub_menu != "d":
    sub_menu = input(
"""---------------Gestión de locales---------------
      a) Crear locales
      b) Modificar local
      c) Eliminar local
      d) Volver
Escoger la opción a la que desee acceder: """)

if sub_menu == "d":
  reinicio()
if sub_menu == "b" or sub_menu == "c":
  separador()
  print("Lo sentimos, esta sección esta en construcción...")
if sub_menu == "a":
  lista = []
  separador()
  

