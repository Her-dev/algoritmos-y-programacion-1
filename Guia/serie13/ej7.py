
class Nodo:
	def __init__(self, dato = None, prox = None):
		self.dato = dato
		self.prox = prox

	def __str__(self):
		return str(self.dato)

class ListaCircular:
	def __init__(self):
		self.prim = None
		self.ult = None
		self.len = 0

	def insert(self, i, x):
		if i < 0 or i > self.len:
			raise IndexError("Posición inválida")

		nuevo = Nodo(x)

		if i == 0:
			if self.len == 0:
				self.prim = nuevo
				self.ult = nuevo
				nuevo.prox = self.prim
			else:
				nuevo.prox = self.prim
				self.prim = nuevo
				self.ult.prox = self.prim

		elif i == self.len:
			self.ult.prox = nuevo
			self.ult = nuevo
			self.ult.prox = self.prim

		else: 
			ant = self.prim
			for pos in range(1, i):
				ant = ant.prox

			nuevo.prox = ant.prox
			ant.prox = nuevo

		self.len += 1

	def append(self, x):
		nuevo = Nodo(x)

		if self.len == 0:
			self.prim = nuevo
			self.ult = nuevo
			self.ult.prox = self.prim
		else:
			self.ult.prox = nuevo
			self.ult = nuevo
			self.ult.prox = self.prim

		self.len += 1

	def remove(self, x):
		if 




		

