def p1 ( a ):
  if a > 0 :
    print ( a )
    p1( a - 1 )
  else:
    print( 'Fin' )
    
p1(6)

