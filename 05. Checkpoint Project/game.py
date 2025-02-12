import random

options = ["Rock✊", "Paper🤚", "Scissors✌️", "Lizard🦎", "Spock🖖"]
selection = 0
player = ""
player_choice = 0
cpu_choice = random.randint(0, 4)
messages = random.randint(0, 9)

win_messages = [
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

lose_messages = [
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

tie_messages = [
    "Well, that was awkward... 😅",
    "A true battle of equals! ⚖️",
    "Nobody won… but nobody lost either! 🤷‍♂️",
    "So close, yet so far! 😬",
    "Great minds think alike! 🧠✨",
    "A perfect stalemate! ♟️",
    "An epic clash… with no winner! ⚔️",
    "Guess you’ll have to settle this later! 😏",
    "You both played like champions! 🏆🏆",
    "A tie? What are the odds?! 🎲"
]

print("==================================================================")
print("=                                                                =")
print("= ¡Welcome to the Rock✊ Paper🤚 Scissor✌️ Lizard🦎 Spock🖖 game! =")
print("=                                                                =")
print("==================================================================")


while True:
    try:
        selection = int(input("Enter 1 to play or 2 to see the rules: "))
        print("------------------------------------------------------------------")
        if selection in [1, 2]:
            break
        else:
            print("Invalid option! Please enter 1 or 2.")
            print("------------------------------------------------------------------")
    except ValueError:
        print("Invalid input! Please enter a number.")
        print("------------------------------------------------------------------")

if selection == 2:
    print("=======================================")
    print("=             Game Rules              =")
    print("=======================================")
    print("=  Rock ✊ crushes Scissors ✌️         =")
    print("=  Scissors ✌️ cuts Paper 🤚           =")
    print("=  Paper 🤚 covers Rock ✊            =")
    print("=  Rock ✊ crushes Lizard 🦎          =")
    print("=  Lizard 🦎 poisons Spock 🖖         =")
    print("=  Spock 🖖 smashes Scissors ✌️        =")
    print("=  Scissors ✌️ decapitates Lizard 🦎   =")
    print("=  Lizard 🦎 eats Paper 🤚            =")
    print("=  Paper 🤚 disproves Spock 🖖        =")
    print("=  Spock 🖖 vaporizes Rock ✊         =")
    print("=======================================")
    

player = input("Whats your name? ")

        
while True:
    print("===================================================================")
    print(f"=  Let's play, {player}! Please choose one of the following options:  =")
    print("===================================================================")
    print("=  1. Rock ✊                                                     =")
    print("=  2. Paper 🤚                                                    =")
    print("=  3. Scissors ✌️                                                  =")
    print("=  4. Lizard 🦎                                                   =")
    print("=  5. Spock 🖖                                                    =")
    print("===================================================================")

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
    messages = random.randint(0, 9)
    print("")
    print(f"{player} selected {options[player_choice]}")
    print(f"CPU selected {options[cpu_choice]}")
  
   
    if player_choice == cpu_choice:
        print(f"{tie_messages[messages]} It's a tie!")
    elif player_choice == 0:    #Rock✊
        if cpu_choice == 1:
            print(f"{lose_messages[messages]} CPU win!")
        elif cpu_choice == 2:
            print(f"{win_messages[messages]} {player} win!")
        elif cpu_choice == 3:
            print(f"{win_messages[messages]} {player} win!")
        else:
            print(f"{lose_messages[messages]} CPU win!")

    elif player_choice == 1:    #Paper🤚
        if cpu_choice == 0:
            print(f"{win_messages[messages]} {player} win!")
        elif cpu_choice == 2:
            print(f"{lose_messages[messages]} CPU win!")
        elif cpu_choice == 3:
            print(f"{lose_messages[messages]} CPU win!")
        else:
            print(f"{win_messages[messages]} {player} win!")
    
    elif player_choice == 2:    #Scissors✌️
        if cpu_choice == 0:
            print(f"{lose_messages[messages]} CPU win!")
        elif cpu_choice == 1:
            print(f"{win_messages[messages]} {player} win!")
        elif cpu_choice == 3:
            print(f"{win_messages[messages]} {player} win!")
        else:
            print(f"{lose_messages[messages]} CPU win!")

    elif player_choice == 3:    #Lizard🦎
        if cpu_choice == 0:
            print(f"{lose_messages[messages]} CPU win!")
        elif cpu_choice == 1:
            print(f"{win_messages[messages]} {player} win!")
        elif cpu_choice == 2:
            print(f"{lose_messages[messages]} CPU win!")
        else:
            print(f"{win_messages[messages]} {player} win!")
            
    elif player_choice == 4:    #Spock🖖
        if cpu_choice == 0:
            print(f"{win_messages[messages]}, {player} win!")
        elif cpu_choice == 1:
            print(f"{lose_messages[messages]} CPU win!")
        elif cpu_choice == 2:
            print(f"{win_messages[messages]} {player} win!")
        else:
            print(f"{lose_messages[messages]} CPU win!")
   
    
    play_again = int(input("Do you want to play again? Enter 1 to play again or 2 to quit: "))
    if play_again == 2:
        print("Thanks for playing! Goodbye!")
        break

