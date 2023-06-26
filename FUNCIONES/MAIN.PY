## primero hacemos uso de la palabra recervada def
## segundo le ponemos un nombre en nuestra  funcion
## establecemos los parametros que resivira nuestra funcion
##( funcion sin parametros)→b→

def saludo():
    
    mensaje="""    
    ====================================================================
    hola este es el mensaje de bienvenida....
    cargando....
    el dota esta lento...
    para cerrar ...
    mi fb esta abierto
    ====================================================================
          
    """
    return mensaje
def suma(numeroUno,numeroDos):
    operacion=numeroUno+numeroDos
    return operacion
primerDato=int(input('Ingrese el primer numero: '))
segundoDato=int(input('Ingrese el segundo numero: '))

print (suma(primerDato,segundoDato))