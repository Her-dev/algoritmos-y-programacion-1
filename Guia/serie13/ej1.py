#Ej 13.1

class Nodo:
	def __init__(self, dato = None, prox = None):
		self.dato = dato
		self.prox = prox

	def __str__(self):
		return str(self.dato)

class ListaEnlazada:
	def __init__(self):
		self.prim = None
		self.len = 0

	def __str__(self):
		actual = self.prim
		cadena = ""

		if actual is None:
			return f"[]"

		while actual:
			cadena += f"{actual.dato}, "
			actual = actual.prox
		cadena = cadena.rstrip(", ")

		return f"[{cadena}]"

	def insert(self, i, x):
		"""Inserta el elemento x, en la posición i"""
		if i < 0 or i > self.len:
			raise IndexError("Posición Inválida")

		nuevo = Nodo(x)

		if i == 0:
			nuevo.prox = self.prim
			self.prim = nuevo

		else:
			ant = self.prim
			for pos in range(1, i):
				ant = ant.prox

			nuevo.prox = ant.prox
			ant.prox = nuevo

		self.len += 1

#Ej 13.2

	def extend(self, otra):
		"""Dada dos ListasEnlazadas, devuelve otra que tenga ambas concatenadas"""
		if otra.prim is None:
			return

		act = self.prim
		while act and act.prox: #Para que no explote si Self.prim es none (lista vacía)
			act = act.prox
		
		act_otra = otra.prim
		while act_otra:
			nuevo = Nodo(dato = act_otra.dato)
			if not act:
				self.prim = nuevo
			else:
				act.prox = nuevo
			act = nuevo
			act_otra = act_otra.prox

#Ej 13.3

	def remover_todos(self, elemento):
		"""Dado un elemento, borra de la lista todas sus apariciones y devuelve cuantos eran"""
		cont = 0 
		ant = None
		act = self.prim

		while act:
			if act.dato != elemento:
				ant = act

			else:
				if not ant:
					self.prim = act.prox
					cont += 1
				else:
					ant.prox = act.prox
					cont += 1

			act = act.prox

		return cont

#Ej 13.4

	def duplicar(self, elemento):
		act = self.prim

		while act:
			if act.dato != elemento:
				act = act.prox

			else:
				nuevo = Nodo(dato = act.dato)
				nuevo.prox = act.prox
				act.prox = nuevo
				act = nuevo.prox

#Ej 13.5

	def filter(self, f):
		act = self.prim
		ant = None

		while act:
			if f(act.dato):
				ant = act
			else:
				if not ant:
					self.prim = act.prox
				else:
					ant.prox = act.prox
			act = act.prox

#Ej 13.6

	def inverte(self):
		act = self.prim
		ant = None
		proximo = None

		while act:
			proximo = act.prox #Guardo la referencia al siguiente ("a la derecha")

			act.prox = ant #Apunto el próximo a la "Izquierda"

			ant = act
			act = proximo

		self.prim = ant

#pre parcialito

	def filtrar_elementos(f):
		act = self.prim
		ant = None

		while act:
			if f(act.dato):
				if not ant:
					self.prim = act.prox
				else:
					ant.prox = act.prox
			else:
				ant = act
			act = act.prox
			
#repaso parcialito

	def eliminar_posiciones(self,lista_posiciones):
		act = self.prim
		ant = None
		i = 0
		pos = 0

		while act:
			if i == len(lista_posiciones):
				break

			if pos == lista_posiciones[i]:
				if not ant:
					self.prim = act.prox
					act = act.prox

				else:
					ant.prox = act.prox
					act = act.prox

				i += 1

			else:
				ant = act 
				act = act.prox

			pos += 1

		if i != len(lista_posiciones) - 1:
			raise IndexError



















