# Este programa muestra primero el listado de categorias de peliculas y pide al usuario
# que introduzca el  código de la categoria de la pelicula y posterior a ello pide que el usuario
# introduzca el número de dias de  atraso, y asi se muestra al final el total a pagar.


# datos de la empresa
Nombre_De_Empresa= "(*_*)TECHNOLOGIES_CRISTIAMS"
print(f"*_* BIENVENIDO A *-* →",(Nombre_De_Empresa), '2023')


# Datos del usuario
Nombre_cliente= input ('Ingrese su nombre ♠ ♠ → : ')
Apellido_Cliente= input('Ingrese suApellido → : ')
DNI= int(input('ingrese DNI: ♠ ♠ ' ))


 
# Definir el listado de categorías de películas con sus códigos y tarifas de atraso

categorias = {
    "A": 20.00, 
    # Categoría A con tarifa de 50 soles por día de atraso
    "B": 35.00, 
    # Categoría B con tarifa de 30 soles por día de atraso
    "C": 20.00 
    # Categoría C con tarifa de 20 soles por día de atraso
}


 # Mostrar el listado de categorías de películas
print("Listado de categorías de películas:")
for categoria, tarifa in categorias.items():
    print(f"Categoría {categoria}: Tacrifa de atraso {tarifa} soles  por día")
    
    
    
 # Pedir al usuario que introduzca el código de la categoría de la película
codigo_categoria = input("Introduce el código de la categoría de la película: ")



 # Validar si el código de categoría existe en el listado
if codigo_categoria in categorias:
    
    
    
    # Pedir al usuario que introduzca el número de días de atraso
    dias_atraso = int(input("Introduce el número de días de atraso: "))
    
    
    
     # Calcular el total a pagar
    tarifa_atraso = categorias[codigo_categoria]
    total_pagar = tarifa_atraso * dias_atraso
    
    
    
     # Mostrar el total a pagar
     
    
    print(f'El Cliente: ',Nombre_cliente,Apellido_Cliente,'Con documento de edentidad: ' ,DNI ,'Debe un total de : ', total_pagar,'nuevos soles')
    print ('♥ ♥¡¡¡¡ GRACIAS POR CONFIAR EN NOSOTROS , LO AGRADECEMOS POR LA PUNTUALIDAD!!!!♥ ♥')
    print(f'la empresa',Nombre_De_Empresa,'LE DESEA UNAS  FELISES FIESTAS PATRIAS PERU !♥ ♥ ♥',)
else:
    print("Código de categoría inválido" )