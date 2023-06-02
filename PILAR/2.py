N1=int(input("ingrese el primer numero 1:  " ))
ops=int(input("Ingresar 1 = SUMAR O 2 = resta:  " ))
N2=int(input("ingrese el numero 2:  " ))
if ops==1:
    print("Suma: " , N1+N2, " :)")
elif ops==2:
    print("RESTA", N1-N2, " :)")
else:
    print( "ERROR AL SELECCIONAR  LA OPERACION")
