#El problema de la rata y el laberinto 

import random 

def elige_camino():
	"""Elije un camino entre tres, con la misma probabilidad"""

	x = random.randrange(30)

	if x < 10:
		return 7

	if 10 <= x < 20:
		return 5 + elige_camino()

	if x >= 20:
		return 3 + elige_camino()

x = 0

for i in range(1000):
	x += elige_camino()

print(f"{x/1000}")

