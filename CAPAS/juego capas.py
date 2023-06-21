while True:
    jugador = input("Elige piedra, papel o tijeras (o 'salir' para terminar el juego): ")
    if jugador == "salir":
        break
    computadora = random.choice(jugadas)
    print("Tu jugada: ", jugador)
    print("Jugada de la computadora: ", computadora)
    if jugador == computadora:
        print("Empate!")
    elif jugador == "piedra":
        if computadora == "papel":
            print("Perdiste!")
        else:
            print("Ganaste!")
    elif jugador == "papel":
        if computadora == "tijeras":
            print("Perdiste!")
        else:
            print("Ganaste!")
    elif jugador == "tijeras":
        if computadora == "piedra":
            print("Perdiste!")
        else:
            print("Ganaste!")