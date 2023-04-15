import sys 
import getpass

def reinicio():
  sys.exit(0)
def separador():
  print(70 * "-")

nombre_usuario = "Administrador"
clave_contraseña = "12345"
intentos = 0

inicio_usuario = input("Ingrese el Usuario: ")
inicio_contraseña = input("Ingrese la contraseña: ")
while (inicio_usuario != nombre_usuario or inicio_contraseña != clave_contraseña) or (len(inicio_usuario) > 100 or len(inicio_contraseña) > 8):
  intentos += 1
  if intentos == 3:
    reinicio()
  separador()
  print("El usuario o la contraseña son inválidos")
  inicio_usuario = input("Ingrese el Usuario: ")
  inicio_contraseña = input("Ingrese la contraseña: ")




















