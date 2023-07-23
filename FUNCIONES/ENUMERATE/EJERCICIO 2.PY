# Definir el catálogo de productos con sus códigos y precios
catalogo = {
    "001": 10,   # Producto 001 con precio de 10 Soles por unidad
    "002": 15,   # Producto 002 con precio de 15 Soles por unidad
    "003": 20    # Producto 003 con precio de 20 Soles por unidad
}


 # Inicializar variables
total_pagar = 0
factura = ""


 # Pedir al usuario que introduzca los códigos y las cantidades de los productos
while True:
    codigo_producto = input("Introduce el código del producto (o 'fin' para terminar): ")
    
    
     # Verificar si el usuario quiere terminar el cálculo de la factura
    if codigo_producto.lower() == "fin":
        break
    
    
     # Verificar si el código de producto existe en el catálogo
    if codigo_producto in catalogo:
        cantidad = int(input("Introduce la cantidad de unidades: "))
        
        
         # Calcular el subtotal del producto y agregarlo a la factura
        precio_unitario = catalogo[codigo_producto]
        subtotal = precio_unitario * cantidad
        factura += f"Código: {codigo_producto}, Cantidad: {cantidad}, Subtotal: {subtotal} soles\n"
        
        
         # Actualizar el total a pagar
        total_pagar += subtotal
    else:
        print("Código de producto inválido")
        
        
 # Mostrar la factura y el total a pagar
print("\nFactura:")
print(factura)
print(f"Total a pagar: {total_pagar} soles")