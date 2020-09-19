def es_potencia_de_dos(n):
	"""Recibe un número natural y devuelve True si es potencia de 2, False si no lo es"""
	while True:
		if n == 0:
			return False
		if n % 2 == 0:
			n = n / 2
			if n == 1:
				return True
		else:
			break

	return False

def suma_potencias_dos(n1,n2):
	"""Dado dos números, devuelve la suma de todas las potencias de dos entre ellos"""
	suma = 0
	for i in range(n1,n2+1):
		if es_potencia_de_dos(i):
			suma += i
	return suma

print(suma_potencias_dos(0,16))



