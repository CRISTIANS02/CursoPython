import random
jugadas = ["piedra", "papel", "tijeras"]
computadora = random.choice(jugadas)
jugador = input("Elige piedra, papel o tijeras: ")
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