#frutas


# print= ('INGRESE EL NOMBRE DE LA FRUTERIA: ')
# NombredeFruteria=[]
# print=('BIENVENIDOS ALA FRUTERIA',NombredeFruteria, 'Usted  es bienvenido')



# enytrada
frutas=[]
indice=0
#proceso
while len(frutas)<5:
   nuevaFruta=input('Ingresa una fruta: ')
   for fruta in frutas:
      if len(nuevaFruta )== len(fruta):
          print('Misma longuitud jilaso en gresa otra frita *-*')
   if nuevaFruta in frutas:
    print(' Esta fruta ya existe imbecil no seas penjedo *_*')
   else:
    frutas.append(nuevaFruta)
print(frutas)

def textoLargo (array):
  LongitudTexto=0
  mostrarFruta=''
  for index in range(0,len(array)):
    if len(array[index])> LongitudTexto:
      LongitudTexto=len(array[index])
      mostrarFruta==array[index]
  return mostrarFruta


#salidaper
print(textoLargo(frutas))

print("la fruta con  la longuitud mas larga es : ",({textoLargo(frutas)}))
print('Su indice positivo es:',indice)
  ### clases de hoy de julio viernes 14 de julio del 2023