
class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

lobos = City("Lobos", "Argentina", "45000", "laguna, paracaidismo, pesca, campo")

print(vars(lobos))