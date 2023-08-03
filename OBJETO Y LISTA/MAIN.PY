# EJERCICO 1
# def miObjeto(objeto):
#     nuevoObjeto={
#         "nombre",
#         "apellido",
#         "edad",
#         "sexo",
#         "direccion"
#     }
#     return objeto
# usuario={
#     "cristian",
#     "poma",
#     "20",
#     "ciempre",
#     "mas alla"

# }



# print(usuario)

# EJERCICIO 2

# def miObjeto(**valores):
#     nuevoObjeto={
#         'nombre':valores['A'],
#         'apellido':valores['B'],
#         'edad':'',
#         'sexo':'',
#         'direccion':''
#     }
#     return nuevoObjeto
# print(miObjeto(A='CRISTIAN',B='POMA',))




# EJERCICIO 3

lista=[2,5,8,4,10]

def sumaNumeros(arrayNumeros):
    totalsuma=0
    for numero in arrayNumeros:
        totalsuma+= numero
    return totalsuma
print(sumaNumeros(lista))

#ejercicio 3  mostrar numero menor
def encontrar_numero_menor(lista):
    return min(lista)
lista = [2, 5, 8, 4, 10]
numero_menor = encontrar_numero_menor(lista)
print("El número menor de la lista es:", numero_menor)




# ejercio 4
lista= [2, 5, 0, 4, 1]
def sumanumeros(arrayNumeros):
    print(sumanumeros(lista))
def numeroMenor (arrayNumeros):
    print(numeroMenor(lista))
def numeroMayor(arrayNumeros):
    mayor=arrayNumeros[0]
    for numero in arrayNumeros:
        if numero > mayor:
            mayor= numero
    return mayor
print (numeroMayor(lista))
            
# crear una funcion en puthon que reciba como como parametro una lista →array y retorne una lista de objetos
# que tendra las caracteristias de cada elemento del array → lista

lista=['aire','mar','tierra']


def lista_Nueva (array):
    lista_2023 = []
    for element in array:
        objet ={
            '1':element.primero,
            '2':element.segundo,
            '':element.tercero
       }
        lista_2023.append(objet)
    return lista_2023
print
        

        
        
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
        
[
    {"Longitud": 6, "valor": "bosque", "posicion": 0},
    {"Longitud": 8, "valor": "montaña", "posicion": 1},
    {"Longitud": 6, "valor": "playa", "posicion": 2}
]



#  03/08/2023
ListaNombre= ['cristian', 'Orlando','jory']
edades=[50,20,10]

def object(ListaNombre,edades):
    lista=[]
    for indice, objeto in enumerate (ListaNombre):
        lista.append({'nombre': objeto, 'edad': edades[indice],'completo':f'{objeto} {edades[indice]}'})
    return lista
print(object(ListaNombre,edades))
    
# crear una funcion que reciba como parametro dos listas y retorne un array de objetos
# con las sigientes caracteristicas
#[{nombre:cristian,edad:50,completo cristian 50},{nombre:Orlando,edad:50,completo orlando 20},
# {nombre:jory,edad:10,completo jory 10}]
