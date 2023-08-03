lista=['bosque','motaña','playa']         
def crear_lista_objetos(array):
    lista_objetos = []
    for elemento in array:
        objeto = {
            "Longitud": len(elemento),
            "valor": elemento,
            "posicion": array.index(elemento)
        }
        lista_objetos.append(objeto)
    return lista_objetos  
        
