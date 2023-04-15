def fun_fact(x):
  if (x==1):
    return 1
  else:
    x = (x*fun_fact(x-1))
    return x
  
num=10

print("El factorial de ", num, "es ",fun_fact(num))
