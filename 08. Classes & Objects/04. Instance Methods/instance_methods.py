
class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, amount): #DEPOSITAR DINERO
    self.balance += amount
    return self.balance

  def withdraw(self, amount): #EXTRAER DINERO
    if amount > self.balance:
      print("Fondos Insuficientes")
    else:
      self.balance -= amount
      return amount
    

  def display_balance(self):
    print(f"Saldo actual: ${self.balance:.2f}") #IMPRIME EL SALDO CON 2 DECIMALES


aldo = BankAccount("Aldo", "Rodriguez", 123, "Caja de Ahorros", 2233, 1000)

aldo.display_balance()
aldo.deposit(800)
aldo.display_balance()
aldo.withdraw(1700)
aldo.display_balance()
