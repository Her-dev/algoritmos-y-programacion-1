def suma_divisores(n):
	"""Devuelve la suma de los divisores de un número n"""
	suma = 0
	for i in range(1, n):
		if n % i == 0:
			suma += i
	return suma

def perfectos(m):
	"""Dado un número m, imprime los primeros m números perfectos (son iguales a la suma de sus divisores)"""
	numero = 1 
	contador = 0

	while contador < m:
		if suma_divisores(numero) == numero:
			print (numero)
			contador += 1

		numero += 1 

def amigos(m):
	"""Dado un número m, imprime las primeras m parejas de números amigos""" 
	contador = 0 
	a = 1 

	while contador < m:
		b = suma_divisores(a)

		if suma_divisores(b) == a and suma_divisores(a) == b:
			print ( f"({a},{b})")
			contador += 1

		a += 1 



		
