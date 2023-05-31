 # Los programas se manejan de manera secuencial

 # Control de flujo

 >Un programa o script de Python es un conjunto de instrucciones analizadas y ejecutadas por el intérprete de arriba hacia abajo y de izquierda a derecha. Cuando todas las instrucciones se han ejecutado, el programa termina. No obstante, contamos con herramientas para alterar el flujo natural del programa: hacer que se saltee una porción de código según se cumpla tal o cual condición, repetir un conjunto de instrucciones, etc.

 ## Condicional
 >Una de estas herramientas es el condicional. A partir de la palabra reservada if, le indicamos a Python que queremos ejecutar una porción de código solo si se cumple una determinada condición (es decir, si el resultado es True, como vimos anteriormente). Consideremos el siguiente 

 #### Ejemplo:

     edad = 30
     if edad >= 18:
         print("Eres un adulto.")

 >Primero definimos una variable *edad*, cuyo valor es un entero, *30*. Luego, a través del condicional indicamos que queremos imprimir "Eres un adulto." en pantalla si se cumple la condición de que el valor de edad sea mayor o igual a *18*.
 
 > En Python se emplean cuatro espacios en blanco para delimitar los bloques de código.
 ### Ejemplo:

    if edad >= 18:
        print("Eres un adulto.")
    print("¡Hola, mundo!")

 >En este código, solamente la segunda línea está dentro del condicional, por cuanto está "indentada" con cuatro espacios. Por el contrario, la tercera línea se ejecuta siempre, independientemente del resultado de la comparación.

 >Ahora bien, para ejecutar un bloque de código en caso que no se cumpla la condición, empleamos la palabra reservada *else*.

    if edad >= 18:
        print("Eres un adulto.")
    else:
        print("Aún no eres un adulto.")

 Por último, podemos especificar otras condiciones en caso que la primera no se cumpla vía *elif*.

    if edad >= 18 and edad < 65:
        print("Eres un adulto.")
    elif edad >= 65:
        print("Eres un adulto mayor.")
    else:
        print("Aún no eres un adulto.")
        

 >Aquí, además, hemos incluido una conjunción vía la palabra reservada and para indicar que, en el primer caso, para que se cumpla la condición, tanto *edad >= 18* como *edad < 65* deben ser verdaderos. Lo contrario de la conjunción es la disyunción, representada por la palabra reservada or.

 ## Interacción con el usuario
 >Python incluye una función llamada input(), similar a print(), pero que exhorta al usuario a escribir algo en la consola, que luego es retornado como una cadena.

    nombre = input("Escribe tu nombre: ")
    print("Hola", nombre)

 > (La función *print()*  nos permite imprimir múltiples objetos en una misma línea separándolos por comas, que luego se traducen en la pantalla como espacios).

 >Así, este código solicita al usuario que escriba su nombre y, una vez obtenido, imprime un saludo personalizado en la pantalla. Sabido esto, podemos adaptar nuestro código anterior para solicitar la edad del usuario y en consecuencia mostrar el mensaje correspondiente.
 ### Ejemplo

    edad = int(input("Escribe tu edad: "))

    if edad >= 18 and edad < 65:
        print("Eres un adulto.")
    elif edad >= 65:
        print("Eres un adulto mayor.")
    else:
        print("Aún no eres un adulto.")

 >Dado que *input()* siempre retorna una cadena de caracteres, debemos primero convertirla a un entero vía la función incorporada *int()* para poder efectuar las comparaciones pertinentes.

 
 ## *condicionales*
 >se realiza algo si se cumple cierta condicion
 ## *Bloques*
 >cuando nosotros utilicemos cualquier control de flujo o funciones  el codigo que se debe ejecutar depues debera nestar definida por bloques o identificaciones

     I.introduccion
     1.1 otro concepto  1.2 otro concepto
     1.2.1. estre es de arriba
 condicion1
    Si se cimple la condicion ejecuta esto
     


EJERCICIOS:

     nombre='cristian'
     mensaje='hola gente'
     print(mensaje)
     print(nombre)
### ejercicio 
     comparacion=20!=20
     if comparacion:
     print('estoy dentro')
     suma=10*20
     multiplicacion =5*20
     print('estoy fuera ')

 ### Ejercicio
     edad=41
     if edad<18:
     print('cana')
    
     if edad>18:
     print ('ya com3 con confianza')

     if edad>40:
     print('nesecita regeneracion')