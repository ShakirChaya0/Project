import sys 
import getpass

def reinicio():
  sys.exit(0)
def separador():
  print(70 * "-")

menu_principal = {
   "1" : "Gestion de locales", 
   "2" : "Crear cuentas de dueños de locales",
   "3" : "Aprobar / Denegarsolicitud de descuento",
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
      3. Aprobar / Denegarsolicitud de descuento
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
    if sub_menu != "a" and sub_menu != "b" and sub_menu != "c" and sub_menu != "d" and sub_menu != 0:
      separador()
      print("La opción que has elegido es incorrecta, intentelo de nuevo ingresando una letra(a, b, c, d)")
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
  separador()
