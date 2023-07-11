# COMO MANEJAR STRING EN PYTHON
EJERCICIO 1 :

    direccion = input ('Ingrese la direccion de domicilio: ')
    print('Usted vive ne la sigiente direccio: ',direccion )

    CONSOLA: 

    Ingrese la direccion de domicilio: Puquio Ayacucho  urb. Los Rosales 223  
    Usted vive ne la sigiente direccion:  Puquio Ayacucho  urb. Los Rosales 223

EJERCICIO 2 :


    direccion = input ('Ingrese la direccion de domicilio: ')
    print('DIRECCION: ', direccion[0], "_",direccion[1])


    CONSOLA: 

    Ingrese la direccion de domicilio: Puquio Ayacucho urb. Los Rosales 223
    DIRECCION:  P _ u




EJERCICIO 3 :

    
    direccion = input ('Ingrese la direccion de domicilio: ')
    print('La cantidad de letras de la direccion es:' , (len(direccion)),'Caracteres.')

    CONSOLA: 


    Ingrese la direccion de domicilio: Puquio Ayacucho Urb, Los Rosales 223
    La cantidad de letras de la direccion es: 36 Caracteres.



EJERCICIO 4 :

    direccion = input ('Ingrese la direccion de domicilio: ')
    if "Ayacucho" in direccion:
        print('Se encontro el valor')
    else: 
        print('No se encontro!!! *_*')


    CONSOLA: 


    Ingrese la direccion de domicilio: Puquio Ayacucho Urb. Los Rosales 223
    Se encontro el valor