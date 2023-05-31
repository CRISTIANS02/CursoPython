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
 >Ten en cuenta, que los valores numéricos, son identificados por Python como tal por no llevar comillas. Si las llevan, se convierten en strings y no son operables matemáticamente hablando:

    numero1 = "10"
    numero2 = "3"

    suma = numero1 + numero2

    print(f'La suma de {numero1} + {numero2} es {suma}.')
### Resultado en la consola :

    La  suma de 10 + 3 = 103

 Fíjate en las variables, he puesto los números como strings.

 Al ser strings, no se suman, se concatenan. El resultado de esto es que se junta el 10 con el 3, devolviendo un 103.

## *La resta en Python*
 >para proceder con la operación de resta, solo tienes que usar el símbolo menos o guion "-".

    numero1 = 10
    numero2 = 3

    resta = numero1 - numero2

    print(f'La resta de {numero1} - {numero2} es {resta}.')
 ### El resultado de consola 
    La resta de  10 - 3 = 7

## *La multiplicación en Python*

 >La multiplicación en Python se realiza con el operador "*" (asterísco).

    numero1 = 10
    numero2 = 3

    multiplicacion = numero1 * numero2

    print(f'La multiplicación entre {numero1} X {numero2} es {multiplicacion}.')
### El resultado en consola 
    La multiplicacion de  10 * 3 = 30

 ## *La división en Python* 

 >La división en Python se efectúa con el símbolo "/".

    numero1 = 10
    numero2 = 3

    division = numero1 / numero2

    print(f'La división de {numero1} entre {numero2} es {division}.')
 ### El resultado en consola 
    La divicion de 10 / 3 = 3.333333333333335

 Ahora que ya sabes lo más básico en matemáticas de Python, vamos a subir un poquito el nivel viendo unas cuantas cosas más.

 ## *El cálculo de potencias en Python*
 >Pasemos a ver el operador para calcular potencias de Python. El operador se escribe con dos asteriscos juntos "**".

    numero1 = 2
    numero2 = 10

    potencia = numero1 ** numero2

    print(f'{numero1} elevado a {numero2} es {potencia}.')

 ### El resultado en la consola
    2 elevado ala 10 es 1024

 Por si no sabes de potencias, aquí tienes el equivalente para realizar esto con la multiplicación convencional:

    potencia = 2 ** 10
    multiplicacion = 2 * 2 * 2 * 2 * 2  *2 * 2 * 2 * 2 * 2 

    print(potencia)
    print(multiplicacion)

### El resultado en consola
    1024
    1024

 como puedes ver, para multiplicaciones repetitivas como esta, es muy útil.

 ## *El operador módulo de Python*

 >El operador módulo de Python nos permite devolver el resto de una división.

 Mira el siguiente código. Fíjate en la variable "division_resto", la cual lleva el operador módulo con el símbolo '%'.

    division_resultado = 10 / 3

    division_resto = 10 % 3

     print(f'El resultado de la división es {division_resultado}.')

    print(f'Nos queda un resto de {division_resto}')n

 ### El resultado en la consola
    El resultado de la divicion es  3.333333333333335.
    nos queda un resto de 1.

 El primer print() imprime el resultado de una división.

 En cambio, con el operador módulo realiza la división y nos da el resto de esta. 10 dividido entre 3 es 3 (redondeando) y nos queda 1 de resto.

 ## Diferencia entre el operador de división y floor division de Python

 >*La división normal de Python (/)*, nos devuelve valores con muchos decimales. Si queremos en algún momento hacer divisiones y obtener solo el resultado con números enteros, utilizaremos el operador floor division (//).

    division_resultado = 10 // 3

    print(f'El resultado de la división es {division_resultado}.')
 ### El resultado en la consola
   
    El resultado de la divicion es: 3

 Ahora, me da un entero en lugar de 3.33333...

 ## *Redondeo a enteros con round de python*
 >Podemos usar el método round() de Python para devolver resultados de números enteros.

 >En este caso, estoy haciendo la división normal, pero al envolverla en un round(), me devuelve un entero y no 3.33333...

 La ventaja de esto frente a floor division, es que además de divisiones, lo puedes emplear con cualquier valor u operación aritmética.

    division_resultado = round(10 / 3)

    print(f'El resultado de la división es {division_resultado}.')

 ### El resultado en la consola
   
    El resultado de la divicion es: 3



 ## operadores de comparacion

 ### Operadores de comparación de Python
 >El operador de comparación se usa para comparar los valores de dos variables y, en función de eso, le proporcionará el resultado como verdadero si la condición se cumple o falso si la condición no se cumple. En este artículo, aprenderá sobre los operadores de comparación de Python y cómo usarlos para comparar dos valores.

 ### Operadores de comparación en Python
 >Hay un total de 6 operadores comparadores diferentes que se mencionan a continuación y que se analizarán en este artículo junto con la sintaxis y los ejemplos. En otros términos, también se conocen como operadores relacionales porque se utilizan para encontrar la relación entre dos variables diferentes.

 ## *Mayor que (>)*
   >El operador “mayor que” es uno de los operadores de comparación de Python que se utiliza para comparar los valores de dos variables poniendo un “>” entre ellos. Si el valor de la variable que está en el lado izquierdo es mayor que en el lado derecho, la salida es verdadera; de lo contrario, será falsa.

Ejemplo:

    x = 10

    y = 5

    x > y

    Output:

    True

    x = 5

    y = 10

    x > y

    Output:

    False

 en lo anterior example del operador Mayor que estamos usando dos variables “x” e “y” y asignándoles valores como x = 10 e y = 5. Cuando el valor de x es mayor que el valor de y, el resultado es Verdadero; de lo contrario, mostrará Falso en x = 5 y y = 10 caso.

 ## *Menos que (<)*
 >El operador “Menor que” es uno de los operadores de comparación de Python que se usa para comparar los valores de dos variables poniendo un “<” entre ellos. Si el valor de la variable que está en el lado izquierdo es menor que en el lado derecho, la salida es verdadera; de lo contrario, será falsa.

 Ejemplo:

    x = 5

    y = 10

    x < y

    Output:

    True

    x = 10

    y = 5

    x < y

    Output:

    False

 Como puedes ver example del operador menor que, estamos usando dos variables “x” e “y” y asignándoles valores x = 5 e y = 10. Cuando el valor de x es menor que el valor de y, el resultado es Verdadero; de lo contrario, mostrará Falso en el caso de x = 10 y y = 5.

 ## *Mayor o igual que (>=)*
 >Este operador combina dos operadores diferentes que son mayor que “>” e igual a “=”. Esto significa que si el valor de la variable es mayor o igual al valor de la variable que está en el lado derecho, el valor será verdadero; de lo contrario, será falso.

 Ejemplo:

    x = 10

    y = 5


    x >= y

    Output:

    True

    x = 10

    y = 10

    x >= y

    Output:

    True

    x = 5

    y = 10


    x >= y

    Output:

    False

 Forma Descripción generada automáticamente con confianza media
 arriba example de “mayor o igual que” ya que los valores de las variables x e y son iguales, la respuesta devuelta es Verdadero o cuando el valor de x es mayor que el valor de y, de lo contrario devuelve Falso. Como práctica, ejecute el código anterior con solo el “pero mas grande que” operador y ver la respuesta.

 ## *Menor que igual (<=)*
 >El operador menor que igual a combina los operadores de comparación igual a y menor que en Python. El operador “menor que igual a” devuelve True si el valor del lado izquierdo   derecho es menor o igual que el valor de la derecha.

   Ejemplo:

    x = 5

    y = 10


    x <= y

    Output:

    True

    x = 10

    y = 10

    x <= y

    Output:

    True

      x = 10

      y = 5


      x <= y

    Output:

    False

 Forma Descripción generada automáticamente con confianza media
 arriba example de “menor o igual que” ya que los valores de las variables x e y son iguales, la respuesta devuelta es Verdadero o cuando el valor de x es menor que el valor de y, de lo contrario devuelve Falso. Como práctica, ejecute el código anterior con solo el “menos que” operador y ver la respuesta.

## *Igual a (==)*
 >El operador igual a en Python devuelve True solo si dos variables bajo consideración son iguales, de lo contrario, el resultado es False. Dos marcas iguales, es decir, “==”, significan el operador “igual a”.

 Ejemplo:

    x = 10

    y = 10


    x == y

    Output:

    True

    x = 5

    y = 10


    x == y

    Output:

    False

Forma Descripción generada automáticamente con confianza media
Como era de esperar, dado que x es igual a y (con valores 10 y 10), la respuesta devuelta es True. De lo contrario, devuelve False en caso de x = 10 y y = 5.
 
 ## *No igual a (!=)*
 >El operador no igual a en Python devuelve True solo si dos variables bajo consideración no son iguales, de lo contrario, el resultado es False. “!=”, significa el operador “no igual a”.

 ### Ejemplo:

    x = 10

    y = 5


    x != y

    Output:

    True

    x = 10

    y = 10


    x == y

    Output:

    False
 Forma Descripción generada automáticamente con confianza media
 ahora en esto example del operador “no igual a” en python solo devuelve True cuando el valor de x no es igual al valor de y. Sin embargo, cuando tanto el valor de x como el de y son iguales, devolverá False.

>Los operadores de comparación se utilizan, como su nombre indica, para comparar dos o más valores. El resultado de estos operadores siempre es True o False.

 ## Operador	Descripción

  >">" *Mayor quE*. True si el operando de la izquierda es estrictamente mayor que el de la derecha; False en caso contrario.   

  >" >="	*Mayor o igual que*. True si el operando de la izquierda es mayor o igual que el de la derecha; False en caso contrario.

  > "<"	*Menor que*. True si el operando de la izquierda es estrictamente menor que el de la derecha; False en caso contrario.

 >"<="	*Menor o igual que*  True si el operando de la izquierda es menor o igual que el de la derecha; False en caso contrario.

  >"=="	*Igual*. True si el operando de la izquierda es igual que el de la derecha; False en caso contrario.

 >"!="	*Distinto*. True si los operandos son distintos; False en caso contrario.
  com=12<13

 ## Operadores logicos
    var = False & False
    opera= False| True>
 ## Operaores aritmeticos
    op=45/23/45*2
    print(opera)
 ## ASIGNACION AUMENTADA
    A=10
    A+=10 ## a=a +10
 ## EJEMPLO 
    suma=false*20
 ## observacion 
    true == 1
    False == 0
 ##  *combinacion de cadenas ( concatenacion)* 
    letra ='hola'+' '+' a todos'
    repetir cadenas 
    cadena='hola'* 5
 ### obtener una cadena en  especifico
    obtenerCadena='hola' 
    texto'descrion del texto :" este es una cita"'
   python asigna a una cadena dos tiposn de indices
   indice posiotivo de derech a izquierda
    empieza con 0
 ### (ojo ) el indice negativo de drecha a izquierda
 ### empieza COPN -1 
 ### QUIERO IMPRIMIR LA LETRA DE MI VARIABLE obtener cadena

    print(obtenerCadena[-3])
    print(mensaje[-2])
    print(texto)
 ## troceado de cadena
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
      indice=5
    iongitud)=6
    longitud=(len ultimoString)
    print(ultimoString[lonitud-1]) ## print (ultimoString[-11])
 ## pertenencia
    pertenencia='H'in 'hola mundo'
    con='a'>'A' → CODIGO ASSCCI
    print(pertenecia)
