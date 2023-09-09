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

# Juego de la Ruleta Andres Arroyave

def jugar_ruleta():
    # Generar un número aleatorio del 1 al 50
    numero_ganador = random.randint(1, 50)
    
    # Generar un número aleatorio del 1 al 100 para determinar el resultado
    resultado = random.randint(1, 100)
    
    # Si el resultado está dentro del 30%, el jugador gana
    if resultado <= 30:
        return numero_ganador, True
    else:
        return numero_ganador, False

def main():
    saldo_inicial = 1000  # Puedes ajustar el saldo inicial como desees
    saldo = saldo_inicial
    
    while saldo > 0:
        print(f"Tu saldo actual es: ${saldo}")
        apuesta = int(input("¿Cuánto quieres apostar? (0 para salir): "))
        
        if apuesta == 0:
            break
        
        if apuesta > saldo:
            print("No puedes apostar más de tu saldo actual.")
            continue
        
        numero_apostado = int(input("Elige un número del 1 al 50 en el que apostar: "))
        
        if numero_apostado < 1 or numero_apostado > 50:
            print("Por favor, elige un número entre 1 y 50.")
            continue
        
        saldo -= apuesta
        numero_ganador, ganador = jugar_ruleta()
        
        if ganador:
            saldo += apuesta * 2  # Si gana, el jugador recibe el doble de su apuesta
            print(f"Ganaste ${apuesta * 2}! El número ganador fue {numero_ganador}.")
        else:
            print(f"Perdiste ${apuesta}. El número ganador fue {numero_ganador}.")
    
    print("Gracias por jugar. Tu saldo final es: ${saldo}")
    
if __name__ == "__main__":
    main()
