import sys

def salir():
    sys.exit(0)

def sep():
    return print("-"*70)

user = "administrador"
contraseña = "12345"


inicio = input("Bienvenido estimado, ¿le interesaría ingresar al programa? (conteste con 'Si' o 'No'): ")

respuesta = inicio.lower()


intentos = 0


if respuesta == "si":
    while intentos < 3:
        login_user = input("Ingrese su nombre de usuario: ")
        login_password = str(input("Ingrese su contraseña: "))
        
        if user == login_user and contraseña == login_password:
            print("Felicidades, has podido ingresar!")
            break
        
        else:
            intentos += 1
            if intentos < 3:
                print("Usuario o contraseña incorrectos. Intenta nuevamente.")
            
    if intentos == 3:
        input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
        salir()

else: 
    input("Entonces que tenga un buen día, hasta luego: ")
    salir()


sep()


menú = {
    1: "Gestion de locales",
    2: "Crear cuentas de dueños locales",
    3: "Aprobar / Denegar solicitud de descuento",
    4: "Gestión de novedades",
    5: "Reporte de utilización de descuentos",
    0: "Salir"
}

gestión_menú = {
    "a": "Crear locales",
    "b": "Modificar local",
    "c": "Eliminar local",
    "d": "Volver"
}

print("Aquí se le mostrará el menú principal: ")

for clave, valor in menú.items():
    print(clave, ":", valor)

comida = 0
indumentaria = 0
perfumería = 0

while True:
    elección = int(input("¿Que parte del menú principal le gustaría ver?: ")) 
    
    if elección > 1:
        
        print("Lo lamentamos pero esta sección está en construcción")
        
    elif elección == 0: 
        
        salir()
        
    else:
        
        for clave, valor in gestión_menú.items():
             print(clave, ":", valor)
        
        while True:
            
            sub_menú = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ")
            sep()
            if sub_menú == "b" or sub_menú == "c":
                print("Lo lamentamos pero esta sección está en construcción")
            
            elif sub_menú == "a":
                sep()
                
                print("Ingrese los datos de los locales que desee crear (máximo tres)")
                nombres = nombre1, nombre2, nombre3 = input("Ingrese los nombres separados por comas, por favor: ").split(",")
                rubros = rubro1, rubro2, rubro3 = input("Ingrese los rubros separados por comas acorde al orden de su nombre: ").split(",")
                ubicaciones = ubi_1, ubi_2, ubi_3 = input("Ingrese las ubicaciones separadas por comas acorde al orden de su rubro: ").split(",")
                
                for rubro in rubros:
                
                  if rubro == "comida":
                        comida += 1
                  elif rubro == "indumentaria":
                        indumentaria += 1
                  elif rubro == "perfumería":
                        perfumería += 1
                        
                if comida > indumentaria and comida > perfumería:
                  print(f"El rubro con más locales es comida, con {comida} locales")
                elif indumentaria > comida and indumentaria > perfumería:
                  print(f"El rubro con más locales es indumentaria, con {indumentaria} locales")
                elif perfumería > indumentaria and perfumería > comida:
                  print(f"El rubro con más locales es perfumería, con {perfumería} locales")
                  
                  
                  
                  
            else:
                print("Volviendo...")
                break
                
                