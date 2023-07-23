## primero hacemos uso de la palabra recervada def
## segundo le ponemos un nombre en nuestra  funcion
## establecemos los parametros que resivira nuestra funcion
##( funcion sin parametros)→b→

#def saludo():
    
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
#def suma(numeroUno,numeroDos):
    operacion=numeroUno+numeroDos
    return operacion
#primerDato=int(input('Ingrese el primer numero: '))
#segundoDato=int(input('Ingrese el segundo numero: '))

#print (suma(primerDato,segundoDato))



###2

def mensaje(resultado):
    
     nuevoMensaje=f"""    
    ====================================================================
    EL RESULTADO DE LA OPERACION
    DE LA SUMA ES :
    {resultado}
    ====================================================================
          
    """
     return nuevoMensaje

def suma(numeroUno,numeroDos):
    operacion=numeroUno+numeroDos
    return mensaje (operacion)
primerDato=int(input('Ingrese el primer numero: '))
segundoDato=int(input('Ingrese el segundo numero: '))

print (suma(primerDato,segundoDato))






# clase de 20 de julio 2023

 # imprimir indice y valor que lo divide entre dos 
# lista=['a','b','c']
# for indice,valor in enumerate(lista):
#   print(indice,valor)
 # imprimir indice y valor que lo divide entre dos 
 
lista=['a','b','c']
for _valor in enumerate(lista):
  print(_valor)
  
  
  
lista=['a','b','c']
for _valor in enumerate(lista):
  if _valor =='i':
    print(_valor)
  
  # imprimir indice y valor que lo divide entre dos 
  
  
  
  
## CREAR UNA LISTA QUEALMACENE LOS NUMEROS DEL 1 AL 10
# CREAR UNA FUNCION QUE ME PERMITA RECIBIR COMO PARAMETRO UNA LISTA,
# LA FUNCION TENDRA QUE RETORNAR UN NUEVO ARRAY CON TODO LOS NUMERO PARES QUE EXISTEN 