def p3 ( a, b ):
  if a > 0 :
    p3 ( a - 1, b + a )
  else:
    print ( b )
    
for i in range (1 , 10):
  print(i = 2)
  p3 (i, 0 )
print ( 'Fin' )