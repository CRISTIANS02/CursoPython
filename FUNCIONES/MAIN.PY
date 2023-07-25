## primero hacemos uso de la palabra recervada def
## segundo le ponemos un nombre en nuestra  funcion
## establecemos los parametros que resivira nuestra funcion
##( funcion sin parametros)→b→

#def saludo():
    
    # mensaje="""    
    # ====================================================================
    # hola este es el mensaje de bienvenida....
    # cargando....
    # el dota esta lento...
    # para cerrar ...
    # mi fb esta abierto
    # ====================================================================
          
    # """
#     return mensaje
# #def suma(numeroUno,numeroDos):
#     operacion=numeroUno+numeroDos
#     return operacion
# #primerDato=int(input('Ingrese el primer numero: '))
# #segundoDato=int(input('Ingrese el segundo numero: '))

# #print (suma(primerDato,segundoDato))



###2

# def mensaje(resultado):
    
#      nuevoMensaje=f"""    
#     ====================================================================
#     EL RESULTADO DE LA OPERACION
#     DE LA SUMA ES :
#     {resultado}
#     ====================================================================
          
#     """
#      return nuevoMensaje

# def suma(numeroUno,numeroDos):
#     operacion=numeroUno+numeroDos
#     return mensaje (operacion)
# primerDato=int(input('Ingrese el primer numero: '))
# segundoDato=int(input('Ingrese el segundo numero: '))

# print (suma(primerDato,segundoDato))






# clase de 20 de julio 2023

 # imprimir indice y valor que lo divide entre dos 
# lista=['a','b','c']
# for indice,valor in enumerate(lista):
#   print(indice,valor)
 # imprimir indice y valor que lo divide entre dos 
 
# lista=['a','b','c']
# for _valor in enumerate(lista):
#   print(_valor)
  
  
  
# lista=['a','b','c']
# for _valor in enumerate(lista):
#   if _valor =='i':
#     print(_valor)




  
  # imprimir indice y valor que lo divide entre dos 
# empresa ={}
# empresa['nombre']=input('ingrese nombre de la empresa : ')
# empresa['ruc']=int(input('ingrese ruc de la empresa : '))
# empresa['direccion']=(input('ingrese direccion a la empresa : '))
# empresa['sucursales']=[]
# while len(empresa['sucursales']) <2 :
#   sucursal = input('ingrese el nombre de la sucursal : ')
#   empresa ['sucursales'].append(sucursal)
#   empresa['horario']={}
#   empresa['horario']['dia'] = input('ingrese el horario del dia : ')
#   empresa['horario']['tarde']=input('ingrese el horario de la tarde : ')
# print(empresa)




#ejercicio 2


# empresa=input('Ingrese el nombre de la empresa: ' )
# ruc=input('Ingrese numero de ruc: ' )
# direccion=input('Ingrese direccion: ' )
# sucursales=[]
# for indice in range(0,3):
#   sucursal=input('Ingrese la sucursal: ' )
#   sucursal.append(sucursal )
# empresa={'nombre':empresa,
#          'ruc':ruc,
#          'direccion':direccion,
#          'horario':horario
         
#          }  



# ejercicio 3

# nombre=input('ingrese el nombre de la empresa: ' )
# ruc=input('Ingrese numero de ruc: ' )
# direccion=input('Ingrese direccion: ' )
# sucursales=input('ingrse las sucursales separado por comas: ' ).split(',')
# horario_dia=input('ingrese el horario de dia: ' )
# horario_tarde=input('ingrese el horario de tarde: ' )

# empresa={'nombre':nombre,
#          'ruc':ruc,
#          'direccion':direccion,
#          'sucursal': sucursales,
#          'horario':{
#            'dia':horario_dia,
#            'noche':horario_tarde
#          }  
# }
# print(empresa)





#ejercicio 3

empresas = []
nombre=input('ingrese el nombre de la empresa: ' )
ruc=input('Ingrese numero de ruc: ' )
direccion=input('Ingrese direccion: ' )
sucursales=input('ingrse las sucursales separado por comas: ' ).split(',')
horario_dia=input('ingrese el horario de dia: ' )
horario_tarde=input('ingrese el horario de tarde: ' )
for i in range(0,3):
  empresa={'nombre':nombre,
          'ruc':ruc,
          'direccion':direccion,
          'sucursal': sucursales,
          'horario':{
            'dia':horario_dia,
            'noche':horario_tarde
          }  
 }
  empresas.append(empresa)
  print(empresas)