import sys 
import getpass

def reinicio():
  sys.exit(0)
def separador():
  print(70 * "-")

sub_menu = 0

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
  nombre_local = input("Ingrese el nombre")



















sub_menu = {
  "a" : "Crear locales",
  "b" : "Modificar local",
  "c" : "Eliminar local",
  "d" : "Volver"
}