#  hacer un programa que pida un numero y calcule su factorial
#ejemplo si ingreso 5
#  de salida me debera imprimir 120

# lista = []
# for _ in range(0,5):
#     dato = input("Ingresa un dato: ")
#     lista.append(dato)
#     print("La lista completa es:")
# print(lista)


# factorial=[]
# for _ in range():
#     numero = int(input("Ingrese un numero: "))
   # ejercicio
# a=2
# def calculaFactorial(n):
#     if n:
#         n=n* calculaFactorial(n-1)
#     else:
#         return n
#     factorial_a = calculaFactorial(a)
# print(f"el factorial de {a} es {factorial_a}")        


#  ejercicio con prof 
numero=int(input('ingtrese el numero: '))
factorial=1
if numero== '0':
    print('l factorial de 0 es 0')
else:
    for num in range(1,numero+1):
        factorial=factorial*num
    print(factorial)
print(factorial)