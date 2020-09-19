from colas_pilas import Pila

class Carta:
	def __init__(self, palo, numero):
		self.palo = palo
		self.numero = numero

class Solitario:
	def __init__(self):
		self.pila = Pila()

	def apilar(self, carta):
		if self.pila.esta_vacia():
			self.pila.apilar(carta)
		
		else:
			anterior = self.pila.ver_ultima()

			if carta.palo != anterior.palo and carta.numero == (anterior.numero - 1):
				self.pila.apilar(carta)

			else:
				raise ValueError("la carta no está permitida en este turno")
				