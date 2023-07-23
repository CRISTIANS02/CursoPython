# ## Los programas se manejan de manera secuencial
# ##control de flujo
# #1. condicionales
# ###se realiza algo si se cumple cierta condicion
# ### bloques
# #### cuando nosotros utilicemos cualquier control de flujo o funciones  el codigo que se debe ejecutar depues debera nestar definida por bloques o identificaciones


# #ejercicio
# #evaluar si es menor de 17 monstrar com mensaje cana si es ma
# # yor a 18 monstara come y si es mayor a 40 monstrar ya esta usado

# #entrada de datos
# #dead= input ('ingrese un edad: ')
# #if edad < 17 :
# #  print('cana')
# #f edad > 40 :
# #  print('ya esta usado')
    
    
# # hacer  un programa que pida al usuario su dni si la longuitud del dni es 8  que pida Su nombre  y lo muestre por consola si la longuitud del dni es mayor o menor a 8 que le  mjestre un mensaje de erorr
# #datos de entrada
# dniUsuario= input(" Ingrese si DNI: ")
# longitudDni=len(dniUsuario)
# #proceso
# if longitudDni== 8 :
#     #entrada
#     nombre=input("Ingresa tu nombre: ")
#     #proceso
#     mensaje=f"""hola bienvenido , {nombre}"""
#     #salida de dato
#     print(mensaje)
# else:
#     print("El dni ingresado es incorrecto ")



# # hacer un programa que pida al usuario ingresar el primer apellido si su apellido tiene en como ultimos caractereslas letras--ez-- mostrar un mensaje que diga casi eres español si los carcteres finales  son --es--  que diga eres casi peruano

# # datos de entrada 
# Apellido= input ("Ingrese su apellido Paterno:  ")
# comparacion=Apellido[-2:]
# if comparacion=='ez' :
#   print("eres casi español")
# if comparacion=='es':
#   print('eres casi peruano')

# ## hacer un programa que le pida aun usuario su dni y compruebe que sea de 8 digitos, si es correcto que sume el primer numero del dni, mostrarpor la pantalla la suma y el resultado
# # ejemplo:
# ## ingresa=12345678
# ## "1+8=9"


# # hacer un programa que permita que el usuario ingrese un año  y me de com respuesta si es bisiesto o no




#  #if 
# vocal= input('ingrese  un a vocal minuscula: ' )
# match vocal:
#   case'a' :
#     print('es una vocal')
#   case'e' :
#     print('es una vocal')
#   case'i' :
#     print('es una vocal')
#   case'o' :
#     print('es una vocal')
#   case'u' :
#     print('es una vocal')
    
    
# #2
# vocales='aeiou'
# vocalmayus='AEIOU'
# ingresevocal=input('Ingrese una vocal minuscula: ')
# if ingresevocal in vocales:
#   print('es una vocal minuscula')
# elif ingresevocal in vocalmayus:
#   print('es una vocal mayuscula')
# else:
#   print('no es una vocal ni minuscula ni mayuscula')
  


# ## 3

# ## 

# ## escriba un programa en python que acepte la opcion de los jugadores en piedra-papel y tijera
# ## entrada person 1 = papel
# ##entrada persona 2 = tijera
# ## salia 'gana la persona 2
# import python.util.Scanner;
#  public class BaseConversion {
#     public static void main(String[] args) {
#         Scanner input = new Scanner(System.in);
#          System.out.print("Enter the number: ");
#         String number = input.nextLine();
#          System.out.print("Enter the base of the number: ");
#         int base1 = input.nextInt();
#          System.out.print("Enter the base to convert to: ");
#         int base2 = input.nextInt();
#          int decimal = Integer.parseInt(number, base1);
#         String result = Integer.toString(decimal, base2);
#          System.out.println("The converted number is: " + result);
#     }
# }




# # crear una lista de cinco colores a cada color que interes  tendra que mostrar
# # por cada consola, solo cuandoencuentre el
# # el color rojo montrara el mensaje nde color encontrado y se termina la ejecucion



# colores =['azul','rojo','negro','verde']

# for color in colores:
#     if color =='rojo':
#         print("encontrado")
#         break
#     print(color)
    
#     #hacer un programa  en python, que debe insertar 5 datos y cuando llegue a los 5 datos deje de pedir y corte
# # la ejecucion y muestre todos los datos
# lista = []
# for _ in range(0,5):
#     dato = input("Ingresa un dato: ")
#     lista.append(dato)
#     print("La lista completa es:")
# print(lista)

#  ## ejercicio resuelto en salon  
 
 







# ### hacer un programa donde pida al usuario un numero luego generar la tabla de multiplicar
# #de dicho numero del 1 hasta el 12
# tablaDe=int(input('ingresa un numero: '))
# for numero in range(1,33):
#     resultado=numero*tablaDe
#     print(f"{numero} * {tablaDe} ={resultado }")
    
    
    
    
# #  hacer un programa que pida un numero y calcule su factorial
# #ejemplo si ingreso 5
# #  de salida me debera imprimir 120
# lista = []
# for _ in range(0,5):
#     dato = input("Ingresa un dato: ")
#     lista.append(dato)
#     print("La lista completa es:")
# print(lista)


# numero




# tarea mostrar la sucesion  fibocci de los  10 primeros numeros




'''frutas'''

# frutas=[]
# while len(frutas)<5:
#   nuevaFruta=input('Ingresa una fruta: ')
#   if nuevaFruta in frutas:
#     print('Esta fruta ya existe imbecil no seas penjedo *_*')
#   else:
#     frutas.append(nuevaFruta)
# print(frutas)

# def textoLargo (array):
#   LongitudTexto=0
#   mostrarFruta=''
#   for index in range(0,len(array)):
#     if len(array[index])> LongitudTexto:
#       LongitudTexto=len(array[index])
#       mostrarFruta==array[index]
#   return mostrarFruta

# print(textoLargo(frutas))
  
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
