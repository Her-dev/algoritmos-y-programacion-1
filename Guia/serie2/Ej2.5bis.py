def par_impar(n):
    """Dado un número entero, devuelve 0 si es par o 1 si es impar"""
    return (n % 2)

print (par_impar(2))
print (par_impar(3))

def impar_par(n):
	"""Dado un número entero, devuelve 1 si es par o 0 su es impar"""
	return (n +1) % 2

print (impar_par(2))
print (impar_par(3))

def long(n):
	"""Dado un número, devuelve el dígito de las unidades"""
	return len(str(n))

print (long(153))
print (long(1000))

def ultimo_decimo(n):
	"""Dado un número n, devuelve su múltiplo de 10 inmediato inferior"""
	return n - n%10

print (ultimo_decimo(153))
print (ultimo_decimo(26))
print (ultimo_decimo(5))
