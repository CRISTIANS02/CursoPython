
#hacer un programa  en python, que debe insertar 5 datos y cuando llegue a los 5 datos deje de pedir y corte
# la ejecucion y muestre todos los datos
lista = []
for _ in range(0,5):
    dato = input("Ingresa un dato: ")
    lista.append(dato)
    print("La lista completa es:")
print(lista)


# ejercio en clase 
lista = []

while len (lista) < 5:
    ingreseDato=input('ingresa in dato: ')
    lista.append(ingreseDato)
print( f"""
      ==============================================
      los datos ingresados son{lista}
      ==============================================
      """)    

