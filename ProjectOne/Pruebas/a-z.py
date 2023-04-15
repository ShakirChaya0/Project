a = input("Ingrese una letra mayuscula: ")
b = input("Ingrese una letra mayuscula: ")
c = input("Ingrese una letra mayuscula: ")

if a < b and b < c:
  print(a,b,c)
elif b < a and a < c:
  print(b,a,c)
elif c < a and a < b:
  print(c,a,b)
elif a < c and c < b:
  print(a,c,b)
elif b < c and c < a:
  print(b,c,a)
elif c < b and b < a:
  print(c,b,a)


