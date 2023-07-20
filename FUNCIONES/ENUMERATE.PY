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
  
  
  
  
## CREAR UNA LISTA QUE ALMACENE LOS NUMEROS DEL 1 AL 10
# CREAR UNA FUNCION QUE ME PERMITA RECIBIR COMO PARAMETRO DICHA LISTA Y QUE RETORNE
#EN UNA NUEVA LISTA INGRESADAA POR EL PARAMETRO

# lista = list(range(1, 21))
# def numeros_pares(array):
#   Nueva_lista=[]
#   for _,num in enumerate(lista):
#      if num%2==0:
#        Nueva_lista.append(num)
#   return Nueva_lista
        
# print(numeros_pares(lista))




# #ejercicio 2

# texto='hola como estas'
# print(list(texto))
# print(texto.split(' '))


#hacer un programa en python que pida al usuario un texto,
#y evaluar con una funcion la cantidad de vocales'a' que tiene el texto



texto = input("Usted ingrese su  texto  de identificacion: ")

def contar_vocales_a (texto):
    contador = 0
    for letra in texto:
        if letra.lower() == 'a':
            contador += 1
    return contador
cantidad_vocales_a = contar_vocales_a (texto)
print("El TOTAL DE VOCALES A ES :", cantidad_vocales_a, "VOCALES 'a'.")
