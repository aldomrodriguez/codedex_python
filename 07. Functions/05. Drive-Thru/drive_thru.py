

menu = ['🍔 Cheeseburger', '🍟 Fries', '🥤 Soda', '🍦 Ice Cream', '🍪 Cookie']

def get_items(x):
  return menu[x - 1]

def welcome():
  print('Welcome to Sonnyboy\'s Diner!')
  print('Here\'s the menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_items(option))