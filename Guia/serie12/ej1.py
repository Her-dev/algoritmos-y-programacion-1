#Implementar la clase Intervalo(desde, hasta) --> tiempo en segundos
def validar_numero(valor):
	"""Si el valor es numérico lo devuele, en caso contrario lanza TypeError"""
	if not isinstance(valor, (int, float)):
		raise ValueError(f"{valor} no es un número")
	return valor

class NoInterseccionError(Exception):
	pass

class Intervalo:
	def __init__(self, desde, hasta):
		self.desde = validar_numero(desde)
		self.hasta = validar_numero(hasta)
		if hasta < desde:
			raise ValueError(f"El parámetro *desde* {desde} debe ser menor que el *hasta* {hasta}")

	def duracion(self):
		return int(self.hasta - self.desde)

	def interseccion(self, otro):
		if self._tiene_interseccion(otro):
			
			#if self._fin_menor(otro):
			#	if self._inicio_menor(otro):
			#		return Intervalo(otro.desde, self.hasta)
			#	return self

			#elif not self._fin_menor(otro):
			#	if self._inicio_menor(otro):
			#		return otro
			#	return Intervalo(self.desde, otro.hasta)
			#BILLY
			
			return Intervalo(max(self.desde, otro.desde), min(self.hasta, otro.hasta))
		raise NoInterseccionError("Los intervalos no tienen interseccion")

	def union(self, otro):
		if self._tiene_interseccion(otro) or self._adyacentes(otro):
			return Intervalo(min(self.desde, otro.desde), max(self.hasta, otro.hasta))

	def _inicio_menor(self, otro):
		return self.desde < otro.desde

	def _fin_menor(self, otro):
		return self.hasta < otro.hasta

	def _tiene_interseccion(self, otro):
		return (self.hasta > otro.desde) and (otro.hasta > self.desde)

	def _adyacentes(self, otro):
		return (self.hasta == otro.desde) or (self.desde == otro.hasta)




