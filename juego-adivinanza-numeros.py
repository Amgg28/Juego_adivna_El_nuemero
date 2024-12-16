
import random


def juego_adivinanza():
    # generar un numero del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("! Bienvenido al juego de adivinanza de numero")
    print("Debes adivinar un numero entre el 1 al 100")
    print("!Intenta adivinarlo!")

    while not adivinado:
        adivinanza = input("Introduzca un numero del 1 al 100:")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"EL numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"EL numero secreto es menor a {adivinanza}")
            else:
                print(
                    f"!Felicitaciones has ganado! EL nuemro {adivinanza} es el numero secreto y lo as logrado en {intentos}intentos"
                )
        else:
            print("Por favor introduzca un numero Valido entre el 1 al 100")


juego_adivinanza()
