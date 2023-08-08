# crear un programa que pida los sigientes datos
# nombres,apellidos,dni,programa de estudio,
# de las unidades didacticas pedira los sigientes datos
# el nombre de la unidad el promedio y la condicion se autocompletara
# en relacion del promedio.
# el objeto tendra la sigiente estructura.

# alumnos={
#   'nombres':'jose',
#   'apellidos':'alvarez escobar',
#   'dni':71458369,
#   'programa_estudio':'arquitectura',
#   'unidades_didacticas':[
#      {'lp':{'promedio':15,'condicion':'aprovado'}},
#      {'hds':{'promedio':2, 'condicion':'aprovado'}}
#         ]
    
# #     }

def obtener_condicion(promedio):
    if promedio >= 13:
        return "Aprobado"
    elif promedio >= 12.5:
        return "Regular"
    else:
        return "Desaprobado"

def ingresar_datos():
    datos = {}

    datos['nombres'] = input("Ingrese su nombre: ")
    datos['apellidos'] = input("Ingrese sus apellidos: ")
    datos['DNI'] = input("Ingrese su DNI: ")
    datos['programa_estudio'] = input("Ingrese el programa de estudio: ")

    unidades_didacticas = []
    cantidad_unidades = int(input("Ingrese la cantidad de unidades didácticas a evaluar: "))

    for _ in range(cantidad_unidades):
        unidad_didactica = {}
        unidad_didactica['nombre_unidad'] = input("Ingrese el nombre de la unidad didáctica: ")
        unidad_didactica['promedio'] = float(input("Ingrese el promedio de la unidad didáctica: "))
        unidad_didactica['condicion'] = obtener_condicion(unidad_didactica['promedio'])
        
        unidades_didacticas.append(unidad_didactica)
    
    datos['unidades_didacticas'] = unidades_didacticas

    return datos

datos_alumnos = []

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos a ingresar: "))

for _ in range(cantidad_alumnos):
    datos_alumnos.append(ingresar_datos())

# Imprimir los datos ingresados
for alumno in datos_alumnos:
    print(alumno)
    
    
    
# ejercicio 2
    
          

alumnos = {
    'nombres': input("Ingrese los nombres del alumno: "),
    'apellidos': input("Ingrese los apellidos del alumno: "),
    'dni': int(input("Ingrese el DNI del alumno: ")),
    'programa_estudio': input("Ingrese el programa de estudio del alumno: "),
    'unidades_didacticas': []
}

while True:
    unidad = input("Ingrese el nombre de la unidad didáctica (o 'salir' para finalizar): ")
    if unidad.lower() == 'salir':
        break
    promedio = float(input("Ingrese el promedio de la unidad didáctica: "))
    
    if promedio >= 13:
        condicion = 'aprobado'
    else:
        condicion = 'desaprobado'
    
    alumnos['unidades_didacticas'].append({unidad: {'promedio': promedio, 'condicion': condicion}})

print(alumnos)  