## Los programas se manejan de manera secuencial
##control de flujo
#1. condicionales
###se realiza algo si se cumple cierta condicion
### bloques
#### cuando nosotros utilicemos cualquier control de flujo o funciones  el codigo que se debe ejecutar depues debera nestar definida por bloques o identificaciones


#ejercicio
#evaluar si es menor de 17 monstrar com mensaje cana si es mayor a 18 monstara come y si es mayor a 40 monstrar ya esta usado

#entrada de datos
#dead= input ('ingrese un edad: ')
#if edad < 17 :
#  print('cana')
#f edad > 40 :
#  print('ya esta usado')
    
    
# hacer  un programa que pida al usuario su dni si la longuitud del dni es 8  que pida Su nombre  y lo muestre por consola si la longuitud del dni es mayor o menor a 8 que le  mjestre un mensaje de erorr
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



# hacer un programa que pida al usuario ingresar el primer apellido si su apellido tiene en como ultimos caractereslas letras--ez-- mostrar un mensaje que diga casi eres español si los carcteres finales  son --es--  que diga eres casi peruano

# datos de entrada 
Apellido= input ("Ingrese su apellido Paterno:  ")
comparacion=Apellido[-2:]
if comparacion=='ez' :
  print("eres casi español")
if comparacion=='es':
  print('eres casi peruano')

## hacer un programa que le pida aun usuario su dni y compruebe que sea de 8 digitos, si es correcto que sume el primer numero del dni, mostrarpor la pantalla la suma y el resultado
# ejemplo:
## ingresa=12345678
## "1+8=9"


# hacer un programa que permita que el usuario ingrese un año  y me de com respuesta si es bisiesto o no




 #if 
vocal= input('ingrese  un a vocal minuscula: ' )
match vocal:
  case'a' :
    print('es una vocal')
  case'e' :
    print('es una vocal')
  case'i' :
    print('es una vocal')
  case'o' :
    print('es una vocal')
  case'u' :
    print('es una vocal')
    
    
#2
vocales='aeiou'
vocalmayus='AEIOU'
ingresevocal=input('Ingrese una vocal minuscula: ')
if ingresevocal in vocales:
  print('es una vocal minuscula')
elif ingresevocal in vocalmayus:
  print('es una vocal mayuscula')
else:
  print('no es una vocal ni minuscula ni mayuscula')
  


## 3

## 

## escriba un programa en python que acepte la opcion de los jugadores en piedra-papel y tijera
## entrada person 1 = papel
##entrada persona 2 = tijera
## salia 'gana la persona 2




persona1=input()








