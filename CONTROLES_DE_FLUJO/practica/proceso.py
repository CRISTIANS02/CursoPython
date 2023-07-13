import entrada
while len(entrada.lista)<5:
   dato =input('ingrese el dato: ')
   entrada.lista.append(dato)
for texto in range(0, len(entrada.lista)): 
    if entrada.lista[texto]=='disco':
        palabra=entrada.lista[texto]
        indice=texto