while True:
    jugador1 = int (input("jugador 1 : 1=piedra, 2= papel, 3=tigera: ") )
    jugador2 = int (input("jugador 2 : 1=piedra, 2= papel, 3=tigera: ") )
    
    if jugador1== 1 and jugador2 == 3:
        print('jugador 1 Gana: piedra gana a tigera')
    elif jugador1 == 2 and jugador2 == 1:
        print('jugador 2 gana: papel gana a piedra')
    elif jugador1 == 2 and jugador2 == 2:
        print('jugador 3 gana: tijera gana a papel')
    elif jugador1== 1 and jugador2 == 3:
        print('jugador 1 Gana: piedra gana a tigera')
    elif jugador1 == 2 and jugador2 == 1:
        print('jugador 2 gana: papel gana a piedra')
    elif jugador1 == 2 and jugador2 == 2:
        print('jugador 3 gana: tijera gana a papel')
    else:
        print("ninguno gana")
        break