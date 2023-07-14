'''Escribir un programa en python para calcular el total a pagar
en una factura de 3 productos, incluyendo IGV.
Al finalizar se debe mostar los nombres de cada producto;
el valor a pagar a cada uno de ellos y el total de la factura.'''



print =input(" ")




print("Ingrese el nombre del producto consumido 1 : ")
consumo1 = input()
print(" cantidad comprada de" ,consumo1)
consumo1_cantidad = int(input())
print(" Valor de la unidad de: ", consumo1)
consumo1_vuelto = int(input())


print("Ingrese el nombre del producto consumido 2 : ")
consumo2 = input()
print(" cantidad comprada de" ,consumo2)
consumo2_cantidad = int(input())
print(" Valor de la unidad de: ", consumo2)
consumo2_vuelto = int(input())



print("Ingrese el nombre del producto consumido  3: ")
consumo3 = input()
print(" cantidad comprada de" ,consumo3)
consumo3_cantidad = int(input())
print(" Valor de la unidad de: ", consumo3)
consumo3_vuelto = int(input())


consumo1_st= consumo1_cantidad * consumo1_vuelto
consumo2_st= consumo2_cantidad * consumo2_vuelto
consumo3_st= consumo3_cantidad * consumo3_vuelto

subtotal= consumo1_st + consumo2_st + consumo3_st
IGV= subtotal * 0.18
TOTAL= subtotal  + IGV
tarjeta= ()
efectivo= ()

print("Usted pagara con: , ",tarjeta, "o : ",efectivo)


print(" El total a pagar por : ",consumo1," es:", consumo1_st )
print(" El total a pagar por : ",consumo2," es:", consumo2_st )
print(" El total a pagar por : ",consumo3," es:", consumo3_st )
print(" El subtotal de la compra fue: ",subtotal)
print("El IGV fue: ", IGV)
print("El total a pagar con IGV es:",TOTAL)
