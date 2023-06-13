
import random
def jugar():
    opciones =['piedra','papel,tijera']
    jugada_usuario =input("Elige piedra,papel o tijera:  ")
    if jugada_usuario not in opciones:
        print(" jugada no valida. Por fabor, elige piedra, papel o tijera. ")
    jugada_computadora= random.choice(opciones)
    print(f"la computadora eligio:{'jugada_computadora'}")
    
    if jugada_usuario == jugada_computadora:
        print("¡¡¡¡¡¡¡¡¡¡empate!!!!!!!!!!")
    elif(jugada_usuario== 'piedra' and jugada_computadora == 'tijera')  or (jugada_usuario == 'papel' and jugada_computadora =='piedra') or (jugada_usuario == 'tigera' and jugada_computadora =='papel'):
        print ( "!!!!!!!!!! Ganaste !!!!!!!!!!")
    else:
        print("¡¡¡¡¡¡¡¡¡¡ perdiste!!!!!!!!!!")