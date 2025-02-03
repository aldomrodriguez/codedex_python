print("BANK OF CODEDEX")

pin = int(input("Enter you PIN"))

while pin != 1234:
  pin = int(input("Incorrect PIN. Enter your PIN again: "))

if pin == 1234:
  print("PIN accepted!")