from colas_pilas import Pila

def cuenta_pila(pila):
	"""Devuelve iterativamente la cantidad de elementos de una Pila sin alterarla"""
	cont = 0
	try:
		x = pila.desapilar()
	except IndexError:
		return 0

	cont = cuenta_pila(pila)

	pila.apilar(x)
	
	return cont + 1


x = Pila()

x.apilar(1)
x.apilar(2)
x.apilar(3)
x.apilar(4)
x.apilar(5)
x.apilar(6)
x.apilar(7)

print(cuenta_pila(x))