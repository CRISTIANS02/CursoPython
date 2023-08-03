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
            
# crear una funcion que reciba como como parametro una lista →array y retorne una lista de objetos
# que tendra las caracteristias de cada elemento del array → lista

lista=['aire','mar','tierra']


def lista (array):
    lista = []
    for elemet in array:
        objet ={
            ''
        }
        
        
        
        

# def create_object_list(array):
#     object_list = []
#     for element in array:
#         object = {
#             "characteristic1": element.attribute1,
#             "characteristic2": element.attribute2,
#             "characteristic3": element.attribute3
#         }
#         object_list.append(object)
#     return object_list