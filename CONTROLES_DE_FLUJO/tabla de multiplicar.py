# hacer un programa donde pida al usuario un numero luego generar la tabla de multiplicar
# #de dicho numero del 1 hasta el 12
tablaDe=int(input('ingresa un numero: '))
for numero in range(1,13):
    resultado=numero*tablaDe
    print(f"{numero} * {tablaDe} ={resultado }")