import random

#Juan Esteban Acevedo (Juego del BlackJack)

# Función para crear una baraja de cartas
def crear_baraja():
    palos = ['Corazones', 'Diamantes', 'Picas', 'Tréboles']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [{'valor': valor, 'palo': palo} for valor in valores for palo in palos]
    random.shuffle(baraja)
    return baraja

# Función para calcular el valor de una mano
def valor_mano(mano):
    valor = 0
    ases = 0
    for carta in mano:
        if carta['valor'] in ['K', 'Q', 'J']:
            valor += 10
        elif carta['valor'] == 'A':
            valor += 11
            ases += 1
        else:
            valor += int(carta['valor'])
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    return valor

# Función para mostrar las cartas de la mano del jugador o la del crupier
def mostrar_mano(mano, ocultar_primera_carta=False):
    for i, carta in enumerate(mano):
        if i == 0 and ocultar_primera_carta:
            print("Carta oculta")
        else:
            print(f"{carta['valor']} de {carta['palo']}")

# Función para jugar una mano
def jugar_blackjack():
    baraja = crear_baraja()
    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_crupier = [baraja.pop(), baraja.pop()]

    print("¡Bienvenido al Blackjack!")

    while True:
        print("\nTus cartas:")
        mostrar_mano(mano_jugador)
        print(f"Total de tu mano: {valor_mano(mano_jugador)}")

        print("\nCarta del crupier:")
        mostrar_mano(mano_crupier, ocultar_primera_carta=True)

        # Verificar si el jugador o el crupier tienen blackjack
        if valor_mano(mano_jugador) == 21:
            print("¡Blackjack! ¡Has ganado!")
            break
        elif valor_mano(mano_crupier) == 21:
            print("El crupier tiene Blackjack. Has perdido.")
            break

        # Opciones del jugador: pedir carta o plantarse
        opcion = input("\n¿Quieres pedir carta (P) o plantarte (PL)? ").strip().lower()

        if opcion == 'p':
            mano_jugador.append(baraja.pop())
            if valor_mano(mano_jugador) > 21:
                print("Te has pasado de 21. Has perdido.")
                break
        elif opcion == 'pl':
            # El crupier juega su mano
            while valor_mano(mano_crupier) < 17:
                mano_crupier.append(baraja.pop())
            print("\nCartas del crupier:")
            mostrar_mano(mano_crupier)
            print(f"Total de la mano del crupier: {valor_mano(mano_crupier)}")

            # Determinar el resultado del juego
            if valor_mano(mano_crupier) > 21:
                print("El crupier se ha pasado de 21. ¡Has ganado!")
            elif valor_mano(mano_crupier) > valor_mano(mano_jugador):
                print("El crupier gana.")
            elif valor_mano(mano_crupier) < valor_mano(mano_jugador):
                print("¡Has ganado!")
            else:
                print("Empate.")
            break
        else:
            print("Opción no válida. Elige 'P' para pedir carta o 'PL' para plantarte.")

# Iniciar el juego
jugar_blackjack()
