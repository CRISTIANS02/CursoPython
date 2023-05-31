#ejercicio N° 1
#evaluar si es menor de 17 monstrar com mensaje cana si es mayor a 18 monstara come y si es mayor a 40 monstrar ya esta usado

#entrada de datos
edad = input ('ingrese un edad: ')
if edad <= 17 :
  print('cana')
if edad >= 40 :
  print('ya esta usado')



# Ejercicio N° 2

## hacer  un programa que pida al usuario su dni si la longuitud del dni es 8  que pida Su nombre  y lo muestre por consola si la longuitud del dni es mayor o menor a 8 que le  mjestre un mensaje de erorr
#datos de entrada


dniUsuario= input(" Ingrese si DNI: ")
longitudDni=len(dniUsuario)
#proceso
if longitudDni== 8 :
    #entrada
    nombre=input("Ingresa tu nombre: ")
    #proceso
    mensaje=f"""hola bienvenido , {nombre}"""
    #salida de dato
    print(mensaje)
else:
    print("El dni ingresado es incorrecto ")


# Ejercicio N° 3:

# hacer un programa que pida al usuario ingresar el primer apellido si su apellido tiene en como ultimos caractereslas letras--ez-- mostrar un mensaje que diga casi eres español si los carcteres finales  son --es--  que diga eres casi peruano


Apellido= input ("Ingrese su apellido Paterno:  ")
comparacion=Apellido[-2:]
if comparacion=='ez' :
  print("eres casi español")
if comparacion=='es':
  print('eres casi peruano')


# Ejercicio N° 4:

## hacer un programa que le pida aun usuario su dni y compruebe que sea de 8 digitos, si es correcto que sume el primer numero del dni, mostrarpor la pantalla la suma y el resultado
# ejemplo:
## ingresa=12345678
## "1+8=9"

dni=input("ingrese su dni: ")
if len(dni)==8:
  print("es correcto")
Elif= "9"
print(dni)
    

# Ejercicio N° 5

# hacer un programa que permita que el usuario ingrese un año  y me de com respuesta si es bisiesto o no

#2023
 
año= input("Ingrese un año: ")
if año % 4 != 0: 
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: 
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	print("Es bisiesto")