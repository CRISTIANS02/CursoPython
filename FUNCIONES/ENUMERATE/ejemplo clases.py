#objeto de datos personales
# objeto={}
# objeto['nombre']= input ('Ingrese su nombre: ' )
# objeto['edad']=int(input('Ingrese su edad: ' ))
# objeto['telefono']=int(input ('Ingrese numero de telefono: ' ))
# objeto['correp']= input('Ingrese su correo electronico: ' )

# print ( objeto)








# 
# crear una lista para crear dos objetos en una lista 

# Lista=[]
# while len(Lista)<=1:
#     objeto={}
#     objeto['nombre']=input('Nombre de mascota: ' )
#     objeto['Edad']=int(input('edad de mascota: ' ))
#     objeto['Croqueta']=input('Coqueta faborita: ' )
#     Lista.append(objeto)
# print(Lista)
    





#ejercicio  2

# Lista=[]
# while True:
#     objeto={}
#     objeto['nombre']=input('Nombre de mascota: ' )
#     objeto['Edad']=int(input('edad de mascota: ' ))
#     objeto['Croqueta']=input('Coqueta faborita: ' )
#     Lista.append(objeto)
#     condicion=input( 'si desea salir escriba escriba: S , si desea continuar : C  ' )
#     if condicion.upper()== 'S':
#         break
   
# print(Lista)


##lower→ }



Lista=[]
while True:
    objeto={}
    objeto['nombre']=input('Nombre de mascota: ' )
    objeto['Edad']=int(input('edad de mascota: ' ))
    
    objeto ['comidas']=[]
    while len(objeto['comidas'])<3:
        comida=input('Ingrese la comida faborita: ' )
        objeto['comidas'] .append(comida)
    Lista.append(objeto)
    condicion=input( 'si desea salir escriba escriba: S , si desea continuar : C  ' )
    if condicion.upper()== 'S':
        break
   
print(Lista)
    
    
    
    
    
    
    
# algoritmos de busqueda
→ bubble sort
→insertion sort
→marge sort
→quick sort
→selection sort
→binary shearch