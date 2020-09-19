from math import gcd

class Fraccion:
	def __init__(self, numerador, denominador):
		self.numerador = numerador
		self.denominador = denominador
		if denominador == 0:
			raise ValueError("El denominador no puede ser cero")

		self.simplificar()

	def __str__(self):
		return f"{self.numerador}/{self.denominador}"

	def __add__(self, otro):
		numerador = self.numerador * otro.denominador + self.denominador * otro.numerador
		denominador = self.denominador * otro.denominador
		return Fraccion(numerador, denominador)

	def __mul__(self,otro):
		return Fraccion(self.numerador * otro.numerador, self.denominador * otro.denominador)

	def simplificar(self):
		n = gcd(self.numerador, self.denominador)
		self.numerador = self.numerador // n
		self.denominador = self.denominador // n