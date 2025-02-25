# Write code below 💖

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f"Sonido de {self.name}")

  def display_details(self):
    print(f"Entrada: {self.entry}, Nombre: {self.name}, Tipo: {self.types}, Descripción: {self.description}, Es capturable? {self.is_caught}")

pikachu = Pokemon(1, "Pikachu", "Eléctrico", "Pokemon roedor. Sus ataques son tan fuertes como un rayo", True)

pikachu.speak()

pikachu.display_details()

