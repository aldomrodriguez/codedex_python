# Write code below 💖
import random

frases = [
  "Don't pursue happiness – create it.", 
"All things are difficult before they are easy.", 
"The early bird gets the worm, but the second mouse gets the cheese.", 
"Someone in your life needs a letter from you.", 
"Don't just think. Act!", 
"Your heart will skip a beat.", 
"The fortune you search for is in another cookie.", 
"Help! I'm being held prisoner in a Chinese bakery!"
]
def fortune():
  random_fortune = random.randint(0, len(frases) -1)
  print(frases[random_fortune])

fortune()
fortune()
fortune()
