
def display_rules():
    border = "=" * 40
    print(border)
    print("=           Game Rules           =")
    print(border)
    rules = [
        "Rock ✊ crushes Scissors ✌️",
        "Scissors ✌️ cuts Paper 🤚",
        "Paper 🤚 covers Rock ✊",
        "Rock ✊ crushes Lizard 🦎",
        "Lizard 🦎 poisons Spock 🖖",
        "Spock 🖖 smashes Scissors ✌️",
        "Scissors ✌️ decapitates Lizard 🦎",
        "Lizard 🦎 eats Paper 🤚",
        "Paper 🤚 disproves Spock 🖖",
        "Spock 🖖 vaporizes Rock ✊"
    ]
    for rule in rules:
        print(f"| {rule.ljust(36)} |")
    print(border)

# Llamar a la función para mostrar las reglas
display_rules()