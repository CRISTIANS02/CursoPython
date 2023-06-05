vocales='aeiou'
ingresevocal=input('Ingrese una vocal minuscula: ')
if len(ingresevocal)== 1:
    if ingresevocal in vocales:
     print('es una vocal minuscula')
    else:
     print('no es una vocal ni minuscula ni mayuscula')
else:
    print(' la longitud es mayor a 1')