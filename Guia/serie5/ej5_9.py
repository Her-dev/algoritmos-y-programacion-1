def multiplo_menor(a,b):
	"""Dados dos números, devuelve cuantos múltiplos del primero hay que sean mas chicos que el segundo"""
	contador = 0
	for i in range(a, b):
		if i % a == 0:
			contador += 1 
	
	return contador

def multiplo_menor_while(a,b):
	"""Dados dos números, devuelve cuantos múltiplos del primero hay que sean mas chicos que el segundo"""
	contador = 0 
	multiplicador = 1

	while True:
		if a * multiplicador >= b:
			break

		contador += 1
		multiplicador += 1

	return contador

"""La solución con el while es la que menos operaciones hace.
El for debe pregutnar por CADA número entre ambos.
El while solo va multiplicando hasta que lo supera """
