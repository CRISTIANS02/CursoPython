## Los programas se manejan de manera secuencial
##control de flujo
#1. condicionales
###se realiza algo si se cumple cierta condicion
### bloques
#### cuando nosotros utilicemos cualquier control de flujo o funciones  el codigo que se debe ejecutar depues debera nestar definida por bloques o identificaciones


#ejercicio
#evaluar si es menor de 17 monstrar com mensaje cana si es mayor a 18 monstara come y si es mayor a 40 monstrar ya esta usado

#entrada de datos
dead= input ('ingrese un edad: ')
if edad < 17 :
  print('cana')
if edad > 40 :
  print('ya esta usado')
    
    
# hacer  un programa que pida al usuario su dni si la longuitud del dni es 8  que pida Su nombre  y lo muestre por consola si la longuitud del dni es mayor o menor a 8 que le  mjestre un mensaje de erorr
#datos de entrada
dniUsuario= input(" Ingrese si DNI: ")
longitudDni=len(dniUsuario)
#proceso
if longitudDni== 8 :
    #entrada
    nombre=input("Ingresa tu nombre: ")
    #proceso
    mensaje=f"""hola bienvenido , {nombre}"""
    #salida de dato
    print(mensaje)
else:
    print("El dni ingresado es incorrecto ")



# hacer un programa que pida al usuario ingresar el primer apellido si su apellido tiene en como ultimos caractereslas letras--ez-- mostrar un mensaje que diga casi eres español si los carcteres finales  son --es--  que diga eres casi peruano
