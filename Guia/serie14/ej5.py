from colas_pilas import Pila

class PilaConMaximo:
	def __init__(self):
		self.pila = Pila()
		self.maximos = Pila()

	def apilar(self, x):
		if self.pila.esta_vacia():
			self.pila.apilar(x)
			self.maximos.apilar(x)

		else: 
			if self.maximos.ver_ultima() < x:
				self.maximos.apilar(x)
			self.pila.apilar(x)

	def desapilar(self):
		if self.pila.ver_ultima() == self.maximos.ver_ultima():
			self.maximos.desapilar()

		return self.pila.desapilar()

	def ver_maximo(self):
		return self.maximos.ver_ultima()


