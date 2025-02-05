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



while True:
    try:
        selection = int(input("Enter 1 to play or 2 to see the rules: "))
        if selection in [1, 2]:
            break
        else:
            print("Invalid option! Please enter 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter a number.")

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
    

player = input("Whats your name? ")
print(f"Let's play {player}!")




        
while True:
    print(f"Hello {player}! Please choose one of the following options: ")
    print("1. Rock✊")
    print("2. Paper🤚")
    print("3. Scissors🖖")
    print("4. Lizard🦎")
    print("5. Spock🖖")

    while True:
        try:
            player_choice = int(input("Enter your choice: ")) - 1
            if player_choice in range(5):
                break
            else:
                print("Select one of the correct options!")
        except ValueError:
            print("Invalid input! Please enter a number.")
            
    cpu_choice = random.randint(0, 4)

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
    
    
    
    play_again = int(input("Do you want to play again? Enter 1 to play again or 2 to quit: "))
    if play_again == 2:
        print("Thanks for playing! Goodbye!")
        break
 
#SI ELIJO OTRA COSA QUE NO SEA UN NUMERO VALIDO?
#DAR DINAMISMO, ANADIENDIENDO FRASES QUE ACOMPANEN TANTO AL GANAR COMO AL PERDER, FELICITANDO, BURLANDOSE O PROVOCANDO.
#PROPONER JUGAR OTRA VEZ, METER EL JUEGO EN UN BUCLE
