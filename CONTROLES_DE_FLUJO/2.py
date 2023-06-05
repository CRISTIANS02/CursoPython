vocales='aeiou'
ingresevocal=input('Ingrese una vocal minuscula: ')
if len(ingresevocal)== 1:
    match ingresevocal:
        case ingresevocal if ingresevocal in vocales:
            print:('es vocal')
  
else:
    print(' la longitud es mayor a 1')