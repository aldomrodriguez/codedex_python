co = float(input("Cuantos Pesos Colombianos te sobraron? ")) * 0.00023
pe = float(input("Cuantos Soles Peruanos te sobraron? ")) * 0.26
br = float(input("Cuantos Reales te sobraron? ")) * 0.16
usd_suma = co + pe + br

print(f'Sobraron {usd_suma:.2f} USD')
