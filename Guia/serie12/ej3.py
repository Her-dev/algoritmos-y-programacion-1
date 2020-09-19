#Implementar la clase vector 
class DimensionError(Exception):
	pass

class Vector:
	def __init__(self, coordenadas): #Las coordenadas son una lista de números
		self.coordenadas = coordenadas

	def __str__(self):
		return f"{self.coordenadas}"

	def __add__(self, otro):
		if self.dimensiones() == otro.dimensiones():
			suma = []
			for i in range(self.dimensiones()):
				suma.append(self.coordenadas[i] + otro.coordenadas[i])
			
			return Vector(suma)
		
		raise DimensionError("Los vectores tienen distinta dimensión, por lo que no pueden sumarse")

	def __mul__(self, numero):
		mul = []
		for i in range(self.dimensiones()):
			mul.append(self.coordenadas[i] * numero)

		return Vector(mul)

	def dimensiones(self):
		return len(self.coordenadas)

