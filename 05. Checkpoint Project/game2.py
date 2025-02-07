import random

# Selección de idioma
while True:
    try:
        idioma = int(input("Selecciona el idioma / Select the language:\n1. Español\n2. English\n"))
        if idioma in [1, 2]:
            break
        else:
            print("Opción inválida. Por favor, selecciona 1 o 2.")
    except ValueError:
        print("Entrada no válida. Ingresa un número.")

if idioma == 1:
    opciones = ["Piedra✊", "Papel🤚", "Tijera✌️", "Lagarto🦎", "Spock🖖"]
    mensajes_ganar = [
        "¡Aplastaste a tu oponente! 🎉",
        "¡La victoria es tuya! 🏆",
        "¡Boom! Eso fue épico, bien jugado. 💥",
        "¡Imparable como siempre! 🔥",
        "¡Solo vibras de ganador! 😎",
        "¡Esa fue una jugada maestra! ♟️",
        "¡Juego terminado para tu rival! 😏",
        "¡Jugaste como un campeón! 🥇",
        "¡Sin piedad, sin arrepentimientos, legendario! 😆",
        "¡Demasiado fácil para ti! 🎮"
    ]
    mensajes_perder = [
        "¡Uf, eso dolió! 😵",
        "¡Mejor suerte la próxima! 🍀",
        "No salió como esperabas... 😅",
        "Luchaste con honor... pero perdiste. ⚔️",
        "Bueno, podría haber sido peor... tal vez. 🤷‍♂️",
        "¡La derrota es solo una lección disfrazada! 📖",
        "¡Game over! Inserta otra moneda. 🎮",
        "No fue tu mejor momento, ¿eh? 😬",
        "¡Cerca, pero no lo suficiente! 🚬❌",
        "Te aplastaron... pero con estilo. 😎"
    ]
    mensajes_empate = [
        "Bueno, eso fue raro... 😅 Es un empate.",
        "¡Un verdadero choque de titanes! ⚖️ Es un empate.",
        "¡Nadie ganó, pero nadie perdió! 🤷‍♂️ Es un empate.",
        "¡Tan cerca y a la vez tan lejos! 😬 Es un empate.",
        "¡Las grandes mentes piensan igual! 🧠✨ Es un empate.",
        "¡Un empate perfecto! ♟️",
        "¡Un choque épico... sin vencedor! ⚔️ Es un empate.",
        "Parece que tendrán que desempatar más tarde. 😏 Es un empate.",
        "¡Ambos jugaron como campeones! 🏆🏆 Es un empate.",
        "¿Un empate? ¡Qué probabilidades! 🎲"
    ]
    nombre = input("¿Cuál es tu nombre? ")
    mensaje_inicio = f"¡Vamos a jugar, {nombre}! Selecciona una opción:"
    mensaje_continuar = "¿Quieres jugar otra vez? Ingresa 1 para sí o 2 para salir: "
    mensaje_despedida = "¡Gracias por jugar! ¡Hasta la próxima!"
    mensaje_invalido = "¡Opción inválida! Por favor, selecciona una opción correcta."
else:
    opciones = ["Rock✊", "Paper🤚", "Scissors✌️", "Lizard🦎", "Spock🖖"]
    mensajes_ganar = [
        "You crushed it! 🎉",
        "Victory looks good on you! 🏆",
        "Boom! That was epic—well played! 💥",
        "Unstoppable as always! 🔥",
        "Winner vibes only—nice one! 😎",
        "That was a master move! ♟️",
        "Game over for your opponent—great job! 😏",
        "You played like a champ! 🥇",
        "No mercy, no regrets—legendary play! 😆",
        "Too easy for you! 🎮"
    ]
    mensajes_perder = [
        "Oof, that was rough! 😵",
        "Better luck next time! 🍀",
        "That didn’t go as planned… 😅",
        "You fought bravely… but lost! ⚔️",
        "Well, that could’ve been worse… maybe. 🤷‍♂️",
        "Defeat is just a lesson in disguise! 📖",
        "Game over! Insert another coin. 🎮",
        "Not your best moment, huh? 😬",
        "Close, but no cigar! 🚬❌",
        "You got wrecked… but in style! 😎"
    ]
    mensajes_empate = [
        "Well, that was awkward... 😅 It's a tie!",
        "A true battle of equals! ⚖️ It's a tie!",
        "Nobody won… but nobody lost either! 🤷‍♂️ It's a tie!",
        "So close, yet so far! 😬 It's a tie!",
        "Great minds think alike! 🧠✨ It's a tie!",
        "A perfect stalemate! ♟️",
        "An epic clash… with no winner! ⚔️ It's a tie!",
        "Guess you’ll have to settle this later! 😏 It's a tie!",
        "You both played like champions! 🏆🏆 It's a tie!",
        "A tie? What are the odds?! 🎲"
    ]
    nombre = input("What's your name? ")
    mensaje_inicio = f"Let's play, {nombre}! Please choose an option:"
    mensaje_continuar = "Do you want to play again? Enter 1 to play again or 2 to quit: "
    mensaje_despedida = "Thanks for playing! Goodbye!"
    mensaje_invalido = "Invalid option! Please select a correct option."

while True:
    print(mensaje_inicio)
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
    
    while True:
        try:
            eleccion_jugador = int(input("Ingresa tu elección: ")) - 1
            if eleccion_jugador in range(5):
                break
            else:
                print(mensaje_invalido)
        except ValueError:
            print(mensaje_invalido)
    
    eleccion_cpu = random.randint(0, 4)
    mensaje = random.randint(0, 9)
    print(f"{nombre} seleccionó {opciones[eleccion_jugador]}")
    print(f"CPU seleccionó {opciones[eleccion_cpu]}")
    
    if eleccion_jugador == eleccion_cpu:
        print(mensajes_empate[mensaje])
    elif (eleccion_jugador - eleccion_cpu) % 5 in [1, 3]:
        print(f"{mensajes_ganar[mensaje]} {nombre} gana!")
    else:
        print(f"{mensajes_perder[mensaje]} CPU gana!")
    
    if int(input(mensaje_continuar)) == 2:
        print(mensaje_despedida)
        break
