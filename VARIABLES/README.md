VARIABLES
> Es un espacio en memoria donde podemos almacenar datos
> nombre="cristian"
>nombre es el identificador del espacio de memoria que vamos 
a usar
> = → es el signo de asignacion que nos indica que vamos a almacenar
> cristian → es el dato que estamos almacenando
>el identificador (nombre) como apunta aun en el espacio de memoria no se puede cambiar o editar.
> sin emabargo el dato que almacena puedamutar en cualquier momento


## Pasos para  declarar una variable:

    1 . Darle un nombre al  identoficador (variable)

    2 . Escribir el operador de asignacion (=)

    3 . Escribir el dado a almacenar

## Reglas para nombrar variables :

 1. Solo pueden tener los siguientes caracteres
     * letras minusculas
     * legtras mayusculas
     *  Digitos
     *  Guiones bajos(_)
 2. Solo deben iniciar con letras guion bajo no con digitos
 3. Solo puede ser una palabra reservada del lenguaje

## EJEMPLO DE VARIABLES VALIDAS


a ="valido"         → 3="invalido" ,
a3= "valido"       → 3a="invalido",
a_b_c ="valido"    → for="invalido",
_abc= "valido"     → wisch="invalido,"
_3a ="valido"      → 2_a ="invalido" ,       
 
## *TAREA*

## Convenciones para nombrar una variable
 >## *Tipos de convenciones de nombres de variables en la programación*
 >En programación, la convención de nombres de variables es una práctica común utilizada para nombrar variables de manera consistente y fácilmente reconocible por otros programadores. Hay varios tipos de convenciones de nombres de variables utilizados en diferentes lenguajes de programación. En este artículo, discutiremos los tipos más comunes de convenciones de nombres de variables utilizados en la programación.
  ##  *Camel Case*
  >*Camel Case* es una convención de nomenclatura popular en la programación. En este método de convención de nombres, las palabras que forman el nombre de la variable se escriben juntas y la primera letra de cada palabra se capitaliza excepto la primera palabra. Por ejemplo :
                                        
     - firstName- lastName
     - phoneNumber
  >Son nombres de variables escritos en Camel Case.
 ## *Snake Case*
 >Snake Case es otra convención de nomenclatura popular en la programación. En este método de convención de nombres, las palabras que forman el nombre de la variable se escriben juntas y están separadas por un guión bajo. Por ejemplo:

     * first_name
     * last_name 
     * phone_number
 >son nombres de variables escritos en Snake Case.
 ## *Pascal Case*
>Pascal Case es similar a Camel Case, pero la primera letra de cada palabra se capitaliza, incluida la primera palabra. Por ejemplo:

     * FirstName
     * LastName
     *  PhoneNumber
>son nombres de variables escritos en *Pascal Case*.

## *Kebab Case*
>*Kebab* Case es similar a *Snake Case*, pero en lugar de un guión bajo, las palabras que forman el nombre de la variable están separadas por un guión. Por ejemplo:
     * first-name
     * last-name
     * phone-number
>son nombres de variables escritos en *Kebab Case*.

## *Upper Case*
>En la convención de nombres de variables en *Upper Case*, todos los caracteres del nombre de la variable se escriben en mayúsculas. Por ejemplo:

      * FIRSTNAME
      * LASTNAME
      * PHONENUMBER
>son nombres de variables escritos en Upper Case.

## *Lower Case*
>En la convención de nombres de variables en Lower Case, todos los caracteres del nombre de la variable se escriben en minúsculas. Por ejemplo:

      *  firstname
      * lastname
      * phonenumber
>son nombres de variables escritos en *Lower Case*.

## *Snake Upper Case*
*Snake Upper* Case es una variante de Snake Case en la que todos los caracteres del nombre de la variable se escriben en mayúsculas. Por ejemplo:
     * FIRST_NAME
     * LAST_NAME
     *  PHONE_NUMBER
>son nombres de variables escritos en *Snake Upper Case.*
## Conclusión
>Las convenciones de nombres de variables son importantes porque ayudan a que el código sea más fácil de leer y entender para otros programadores. Los diferentes tipos de convenciones de nombres de variables tienen diferentes propósitos y se utilizan en diferentes lenguajes de programación. Es importante elegir una convención de nombres de variables que sea consistente con la convención utilizada en el lenguaje de programación y la comunidad de programación en la que se trabaja.
 ## Contatantes  y como se declara  en python
 ## *Constantes en Python*
 >*Python* *no tiene una sintaxis dedicada para la declaración de constantes.* Por tanto, tampoco tiene constantes en el sentido estricto de la palabra.
 Así, para definir una constante en Python tienes que usar una variable y asumir que nunca va a cambiar.

>Para definir constantes y para poder indicar a otros programadores que un determinado valor debe ser tratado como una constante es necesario utilizar la convención de que su nombre ha de ir en mayúsculas. Esto queda claro en el PEP 8.

>De esta manera, si queremos declarar algunas constantes, como el valor del número pi, el número de segundos de una hora o la anchura de un componente determinado podríamos hacer lo siguiente:

        PI = 3.14592
        SEGUNDOS_HORA = 3600
        ANCHURA_VENTANA = 760

        print(f'{PI=}')
        print(f'{SEGUNDOS_HORA=}')
        print(f'{ANCHURA_VENTANA=}')
*Resultado:*

        PI=3.14592
        SEGUNDOS_HORA=3600
        ANCHURA_VENTANA=760
>Si te fijas no hay ninguna diferencia respecto de crear una variable y asignarle un valor, excepto por el nombre, que va todo en letras mayúsculas. Solo por este hecho de ir en letras mayúsculas ya se está comunicando que esos nombres en cuestión deben ser tratados como constantes y que, por tanto, no se les debe asignar otro valor en ninguna otra parte del código. Es más, de hacer eso, podrían surgir comportamientos inesperados y, probablemente, erróneos.
Es importante atender a las reglas para dar nombre a las variables:

>Deben estar compuestas de letras mayúsculas y números. No pueden empezar por un número.
Se usa el carácter de subrayado o barra baja para separar distintas palabras dentro del mismo nombre. También se pueden usar como primer carácter del nombre, si quieres comunicar que la constante solo debe ser usada en el módulo que la contiene (constante privada).
Pueden ser de cualquier longitud.
Recuerda que los nombres de variables y constantes deben ser identificativos. Es mejor usar un nombre largo y descriptivo que uno que pueda resultar ambiguo o del que no se entienda su intención. Intenta evitar abreviaturas en los nombres de las constantes.
Otra recomendación es definir las constantes al principio del fichero de programa, después de los import. Esto dará información de qué constantes se usarán en el mismo.
Como podemos asumir que las constantes no cambiarán podemos hacer uso de ellas de manera global. Por lo tanto, no es necesario pasarlas como parámetros a las funciones que las necesiten (si tienen acceso a ellas).

## *Constantes integradas*
>Existen una serie de constantes integradas en Python que son constantes de verdad, constantes estrictas. No se puede cambiar sus valores. Las principales son las siguientes:
True y False. Que son los valores booleanos que ya conocemos.
None. Que representa la idea de null o ningún valor en Python.
Ellipsis o .... Se usa, principalmente, para indicar en tu programa que falta código por escribir. También lo puedes usar para reemplazar a pass.
Si intentas cambiar el valor de algunas de estas constantes obtendrás el error SyntaxError:
>>> True = 1
  File "<stdin>", line 1
    True = 1
    ^^^^
SyntaxError: cannot assign to True
>>> ... = 10
  File "<stdin>", line 1
    ... = 10
    ^^^
SyntaxError: cannot assign to ellipsis here. Maybe you meant '==' instead of '='? 

>Sería interesante tener un mecanismo para lograr este efecto en Python, pero no lo hay. Lo que sí podemos es intentar simularlo. Sigue leyendo…
## Constantes con el decorador @property
>El decorador @property nos permite establecer y asociar métodos getters y setters a un atributo.

>Sin entrar demasiado en detalle en este decorador, pues no es el objetivo de este artículo, a @property le podemos indicar cuáles serán los métodos encargados de gestionar el atributo en cuestión.
>El decorador proviene de la función integrada property(), sobre la cuál puedes leer más en la documentación oficial.

>El pequeño truco aquí es que no definiremos ningún atributo ni ningún método set. Solo crearemos un método get cuyo nombre será el de la constante que queremos definir. Esto simula nuestra constante, pues no podemos darle valor a nuestro método.

>Veamos un ejemplo con con la constante PI. Vamos a crear una clase llamada Constante:

>class Constantes:

    @property
    def PI(self):  # aquí definimos la constante
        return 3.141592
        constantes = Constantes()  # creamos el objeto Constantes
        print(constantes.PI)  # accdemos a la constante PI
        constantes.PI = 10  # intentamos alterar la constante
>Como ves, creamos nuestro método PI que actuará como una constante devolviendo siempre el mismo valor. No hay ningún atributo definido. Si intentamos alterar el valor de PI obtendremos un error.

El código anterior muestra el siguiente resultado:

        3.141592
        Traceback (most recent call last):
        AttributeError: can't set attribute 'PI'
>Pero hay un problema. @property crea un atributo de clase en Constantes que es un objeto de la clase property. Esto hace que todo funcione. Pero podríamos alterar ese atributo, para darle un nuevo valor, con lo que el objeto property desaparecería y en su lugar tendríamos un valor cualquiera. Si después accediéramos de nuevo a constantes.PI obtendríamos ese nuevo valor. De forma que esta solución no es perfecta.

Lo vemos:

    constantes = Constantes()  # creamos el objeto Constantes

    print(constantes.PI)  # accedemos a la constante PI

    Constantes.PI = 100  # alteramos el atributo de clase

    print(constantes.PI)  # accedemos a la supuesta constante PI, pero...
Ten esto muy en cuenta.

Vamos a ver otra aproximación que tiene más o menos el mismo problema.

Constantes con el atributo __slots__
Las clases de Python permiten definir un atributo especial de clase que contiene una secuencia de nombres que funcionarán como los atributos de los objetos de esa clase. Es el atributo __slots__.

Si este atributo está definido no se pueden añadir más atributos de instancia a la clase. Al no definir el atributo __dict__ dentro de __slots__, este tampoco se crea por defecto y se evita que se puedan añadir otros atributos.

Si quieres más información sobre __slots__ puedes leer la documentación oficial de Python.

Así, utilizando este atributo puedes crear una clase que no admita otros atributos. Además, crearemos un atributo de clase por cada constante que necesitemos y le daremos los valores que deseemos.
Ahora podemos acceder a esos atributos a través de instancias de esa clase, pero no podremos modificarlos. Lo vemos:

class Constantes:

    __slots__ = ()
    PI = 3.141592


constantes = Constantes()   # creamos el objeto Constantes

print(constantes.PI)  # accedemos a la constante

constantes.PI = 100  # intentamos alterar el valor de la constante
Esto muestra por pantalla un mensaje similar al siguiente:

    3.141592
    Traceback (most recent call last):
   ...
AttributeError: 'Constantes' object attribute 'PI' is read-only
Se nos dice que el atributo PI es de solo lectura.

Listo, ya tenemos nuestra constante. Pero tenemos el mismo problema que en el caso anterior. ¿Qué pasa si intentamos alterar el atributo de clase?

     constantes = Constantes()   # creamos el objeto Constantes

     print(constantes.PI)  # accedemos a la constante

     Constantes.PI = 100  # alteramos el valor del atributo de clase

    print(constantes.PI)  # accedemos a la supuesta constante
Y obtendremos lo siguiente:

      3.141592
     100
Otra solución imperfecta.

Vamos con otra posibilidad.

## Constantes con namedtuple
>La función namedtuple de la librería estándar collections nos permite crear tuplas (recordemos que las tuplas son inalterables) y ponerle un nombre a cada valor de las mismas.

>Además nos permite acceder a los valores utilizando la notación del punto y el nombre del valor de la tupla en lugar de usar la notación de corchetes.

>Puedes leer más sobre namedtuple en la documentación oficial de collections.

>Vamos entonces a crear una tupla con tantos valores como constantes necesitemos (o varias tuplas de un solo valor, o una combinación de ambas estrategias). A cada valor le pondremos el nombre de la constante representada.

>Para ello primero debemos invocar a la función namedtuple que necesitará al menos dos parámetros. El nombre del tipo de datos que representará esa tupla (le pondremos Constantes) y el nombre de, al menos, una constante.

>La llamada a namedtuple nos devuelve otra función que necesitará tantos parámetros como nombres de constantes hayamos indicado, así que la invocaremos indicando los valores de dichas constantes.

>Y ya podemos usar nuestra tupla con nombres con sus constantes (en este caso solo una):

    from collections import namedtuple

    constantes = namedtuple('Constantes', 'PI')(3.141592)  # creamos la tupla con nombres

    print(constantes.PI)  # accedemos al valor de nuestra constante

    constantes.PI = 100  # intentamos alterar su valor
Y nuevamente tendremos un error al intentar alterar el valor de PI de este tipo: AttributeError: can't set attribute.

Pero… de nuevo el problema de siempre. namedtuple nos ha creado una clase Constantes que contiene un atributo de clase llamado PI. Ese atributo es una referencia a la función _tuplegetter definida en el módulo collections.

¿Qué pasa si alteramos el valor de dicho atributo de clase? Lo podemos hacer así: constantes.__class__.PI = 100. Que a partir de entonces perdemos el acceso al valor definido en nuestra tupla en favor del nuevo valor asignado a PI.

Otra solución que tampoco es perfecta.
## Constantes con *@dataclass*
>El decorador @dataclass nos permite crear clases de tipo registro que contienen solo datos principalmente. Lo interesante es que añade a nuestra clase todos los métodos (métodos dunder, que comienzan y acaban con __) de gestión de los objetos a partir de los atributos de clase definidos, de forma que la velocidad de desarrollo se incrementa. Puede leer sobre las clases de datos en el PEP 557 y en la documentación oficial.

>Además, el decorador permite un parámetro denominado frozen que permite hacer los objetos de dicha clase inmutables, es decir, que no se pueda alterar el valor de sus atributos. Dicho de otra manera, logramos tener objetos cuyos valores son constantes.

>Vamos a ver cómo usaríamos el decorador para definir nuestra constante PI:

        from dataclasses import dataclass

        @dataclass(frozen=True)
        class Constantes:
       PI = 3.141592

    constantes = Constantes()  # creamos nuestro objeto de constantes

    print(constantes.PI)  # accedemos al valor de la constante

    constantes.PI = 100  # intentamos alterar la constante
Y tendremos un resultado similar a:

    3.141592
    Traceback (most recent call last):
    dataclasses.FrozenInstanceError: cannot assign to field 'PI'
>Bueno, creo que a estas altura, si te has leído el resto de alternativas, te puedes ir imaginando lo que pasa. Haz tú mismo la prueba de intentar alterar el atributo de clase PI y obtendrás los resultados de las anteriores aproximaciones.

Hay más opciones, pero voy a parar aquí. No tiene sentido seguir.

## Conclusiones
>La conclusión aquí es evidente: no existen las constantes estrictas en Python y tampoco se pueden simular a la perfección. Cada alternativa para hacerlo tiene sus problemas.

>Hay que entender que, conceptualmente, sí que existen las constantes en Python. Es nuestro deber ser fiel a la filosofía de Python en la que aquellas variables definidas con mayúsculas pasan a ser constantes y no pueden ser modificadas.

>También debemos instruir a aquellos desarrolladores con los que trabajemos para que entiendan la manera de trabajar con Python (al menos en lo que a constantes se refiere).

>Si es necesario, documentaremos el código para evitar problemas y posibles modificaciones de estas constantes.

>Y nada más, si te ha parecido de utilidad esta entrada, o si has aprendido algo, considera suscribirte a la lista de correo de Código Pitón. Te llegarán regalitos nada más suscribirte y trucos y consejos de vez en cuando.