def domino_pro (n):
	"""imprime por pantalla las fichas (al estilo domino) de un juego que tenga un numero n de fichas"""
	for i in range (n+1):
		for x in range (i+1):
			print (i, "|", x)

domino_pro(8)