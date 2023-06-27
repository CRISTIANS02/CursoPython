#lista=[]
#print(lista)
#primerDato=input('ingresa una fruta: ')
#lista.append(primerDato)
#print(lista)
#segundoDato=input('Ingrese una segunda fruta: ')
#lista.append(segundoDato)
#print(lista)

    
#crear un programa que me deje  ingresar datos en una lista vacia
#en caso que el usuario ingrese la palabra 'si' el programa dejara 
# de pedir datos y me mostrara la lista con todos los datos
##ejercicio 1
lista = []
while True:
    dato = input("Ingresa un dato: ")
    lista.append(dato)
    if dato.lower() == "si":
        lista.pop() 
# Elimina la palabra "si" de la lista
        break
print("La lista completa es:")
print(lista)

#ejercicio 2 
lista=[]
while condicion:
    pedirDato=input('Ingrese un dato: ')
    if pedirDato == 'si':
        condicion=false
    lista.append(pedirDato)
print(list)

lista = []
while True:
    dato = input("Ingresa un dato: ")
    lista.append(dato)
    if dato.lower() == "si":
        lista.pop()  
# Elimina la palabra "si" de la lista
        break
print("La lista completa es:")
print(lista)




##debe insertar 5 datos cuando me llegue a 5 datos deje de pedir  corte la ejecucion y muestre lista de todo
#hacer un programa  en python, que debe insertar 5 datos y cuando llegue a los 5 datos deje de pedir y corte
# la ejecucion y muestre todos los datos