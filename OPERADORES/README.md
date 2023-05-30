#  Operaciones con numeros 

  ## *La suma, resta, multiplicación y división*
 >Empecemos por la suma. Para sumar en Python, hay que utilizar el operador "+". Es el mismo que empleamos en la concatenación. Si lo usas con dos strings, los concatena, en cambio, si lo empleas con valores numéricos, los suma.
 ### Declaración de dos valores numéricos
    numero1 = 10
    numero2 = 3

 ### Se realiza la operación de suma. Almacena un 13 (10 + 3).
    suma = numero1 + numero2

 ### Se imprimen los valores de cada variable y el resultado de la suma.
    print(f'La suma de {numero1} + {numero2} es {suma}.')

### Resultado en la consola :
    la suma de 10+3=13
 Analicemos el código. Primero almaceno dos números en variables para operar con ellos.

 En la variable "suma", realizo la operación de sumar el valor de las dos variables (10 + 3).

 En el print() he utilizado el formateo de strings para mostrar los valores de las variables como quiera.

## *Números en strings*
 Ten en cuenta, que los valores numéricos, son identificados por Python como tal por no llevar comillas. Si las llevan, se convierten en strings y no son operables matemáticamente hablando:

    numero1 = "10"
    numero2 = "3"

    suma = numero1 + numero2

    print(f'La suma de {numero1} + {numero2} es {suma}.')
### Resultado en la consola :

    La  suma de 10 + 3 = 103

 Fíjate en las variables, he puesto los números como strings.

 Al ser strings, no se suman, se concatenan. El resultado de esto es que se junta el 10 con el 3, devolviendo un 103.

## *La resta en Python*
 para proceder con la operación de resta, solo tienes que usar el símbolo menos o guion "-".

    numero1 = 10
    numero2 = 3

    resta = numero1 - numero2

    print(f'La resta de {numero1} - {numero2} es {resta}.')
 ### El resultado de consola 
    La resta de  10 - 3 = 7

## La multiplicación en Python

 La multiplicación en Python se realiza con el operador "*" (asterísco).

    numero1 = 10
    numero2 = 3

    multiplicacion = numero1 * numero2

    print(f'La multiplicación entre {numero1} X {numero2} es {multiplicacion}.')
### El resultado en consola 
    La multiplicacion de  10 * 3 = 30

 





## operadores de comparacion
>Los operadores de comparación se utilizan, como su nombre indica, para comparar dos o más valores. El resultado de estos operadores siempre es True o False.

Operador	Descripción
## → >Mayor que. True si el operando de la izquierda es estrictamente mayor que el de la derecha; False en caso contrario.   
## → >=	Mayor o igual que. True si el operando de la izquierda es mayor o igual que el de la derecha; False en caso contrario.
<	Menor que. True si el operando de la izquierda es estrictamente menor que el de la derecha; False en caso contrario.
<=	Menor o igual que. True si el operando de la izquierda es menor o igual que el de la derecha; False en caso contrario.
==	Igual. True si el operando de la izquierda es igual que el de la derecha; False en caso contrario.
!=	Distinto. True si los operandos son distintos; False en caso contrario.
com=12<13

# Operadores logicos
var = False & False
opera= False| True>
# Operaores aritmeticos
op=45/23/45*2
print(opera)
# ASIGNACION AUMENTADA
A=10
A+=10 ## a=a +10
## EJEMPLO 
suma=false*20
## observacion
##true == 1
##False == 0
# combinacion de cadenas ( concatenacion)
letra='hola'+' '+' a todos'
##repetir cadenas 
cadena='hola'* 5
##obtener una cadena en  especifico
obtenerCadena='hola' 
texto'descrion del texto :" este es una cita"'
##python asigna a una cadena dos tiposn de indices
#indice posiotivo de derech a izquierda
### empieza con 0
## el iondice negativo de drecha a izquierda
### empieza COPN -1
#QUIERO IMPRIMIR LA LETRA DE MI VARIABLE obtener cadena

print(obtenerCadena[-3])
print(mensaje[-2])
print(texto)
#troceado de cadena)
trocear='un mensaje'
print(trocear[2:])
print(trocear[3:6])
print(trocear[:-3])
#[inicio:final +1]
#[inicio:inicio negativo]+

ultimoString='texto largo'
ejemplo='123456'
len(ejemplo)##6
## cuando  es la cantidad de indices
##indice=5
##liongitud)=6
longitud=(len ultimoString)
print(ultimoString[lonitud-1]) ## print (ultimoString[-11])
#### pertenencia
pertenencia='H'in 'hola mundo'
con='a'>'A' → CODIGO ASSCCI
print(pertenecia)
