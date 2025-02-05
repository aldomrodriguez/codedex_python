import random

options = ["Rock✊", "Paper🤚", "Scissors✌️", "Lizard🦎", "Spock🖖"]
selection = 0
player = ""
cpu = ""
player_choice = 0
cpu_choice = random.randint(0, 4)

print("==================================================================")
print("=                                                                =")
print("= ¡Welcome to the Rock✊ Paper🤚 Scissor✌️ Lizard🦎 Spock🖖 game! =")
print("=                                                                =")
print("==================================================================")



while selection != 1 and selection != 2:
    selection = int(input("Enter 1 to play or 2 to see the rules: "))
    
if selection == 2:
    print("Rules:")
    print("Rock✊ crushes Scissors✌️")
    print("Scissors✌️ cuts Paper🤚")
    print("Paper🤚 covers Rock✊")
    print("Rock✊ crushes Lizard🦎")
    print("Lizard🦎 poisons Spock🖖")
    print("Spock🖖 smashes Scissors✌️")
    print("Scissors✌️ decapitates Lizard🦎")
    print("Lizard🦎 eats Paper🤚")
    print("Paper🤚 disproves Spock🖖")
    print("Spock🖖 vaporizes Rock✊")
    
elif selection == 1:
    player = input("Whats your name? ")
    print(f"Let's play {player}!")
 

print(f"Hello {player}! Please choose one of the following options: ")
print("1. Rock✊")
print("2. Paper🤚")
print("3. Scissors🖖")
print("4. Lizard🦎")
print("5. Spock🖖")
player_choice = int(input("Enter your choice: ")) - 1
print(f"{player} selected {options[player_choice]}")
print(f"CPU selected {options[cpu_choice]}")


if player_choice == cpu_choice:
    print("It's a tie!")
elif player_choice == 0:    #Rock✊
    if cpu_choice == 1:
        print(f"{cpu} win!")
    elif cpu_choice == 2:
        print(f"{player} win!")
    elif cpu_choice == 3:
        print(f"{player} win!")
    else:
        cpu_choice == 4
        print(f"{cpu} win!")

elif player_choice == 1:    #Paper🤚
    if cpu_choice == 0:
        print(f"{player} win!")
    elif cpu_choice == 2:
        print(f"{cpu} win!")
    elif cpu_choice == 3:
        print(f"{cpu} win!")
    else:
        cpu_choice == 4
        print(f"{player} win!")
 
elif player_choice == 2:    #Scissors✌️
    if cpu_choice == 0:
        print(f"{cpu} win!")
    elif cpu_choice == 1:
        print(f"{player} win!")
    elif cpu_choice == 3:
        print(f"{player} win!")
    else:
        cpu_choice == 4
        print(f"{cpu} win!")

elif player_choice == 3:    #Lizard🦎
    if cpu_choice == 0:
        print(f"{cpu} win!")
    elif cpu_choice == 1:
        print(f"{player} win!")
    elif cpu_choice == 2:
        print(f"{cpu} win!")
    else:
        cpu_choice == 4
        print(f"{player} win!")
        
elif player_choice == 4:    #Spock🖖
    if cpu_choice == 0:
        print(f"{player} win!")
    elif cpu_choice == 1:
        print(f"{cpu} win!")
    elif cpu_choice == 2:
        print(f"{player} win!")
    else:
        cpu_choice == 3
        print(f"{cpu} win!")
 
#SI ELIJO OTRA COSA QUE NO SEA UN NUMERO VALIDO?
#DAR DINAMISMO, ANADIENDIENDO FRASES QUE ACOMPANEN TANTO AL GANAR COMO AL PERDER, FELICITANDO, BURLANDOSE O PROVOCANDO.
#PROPONER JUGAR OTRA VEZ, METER EL JUEGO EN UN BUCLE
