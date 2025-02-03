altura = int(input("¿Cuál es tu altura en cm? "))
creditos = int(input("¿Cuantos creditos tenes? "))

if altura >= 137 and creditos >= 10:
  print('Disfruta del viaje!')

elif altura < 137 and creditos >= 10:
  print('No tienes suficiente altura')

elif altura >= 137 and creditos < 10:
  print('No te alcanzan los creditos!')
else:
  print('No tienes altura y creditos suficientes')