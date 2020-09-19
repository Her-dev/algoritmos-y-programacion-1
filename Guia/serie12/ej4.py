PERMITIDOS = (1, 2, 5, 10, 20, 50, 100, 200, 500 , 1000)

class Caja:
	def __init__(self, caja): #caja es un diccionario 
		self.caja = caja
		for k in caja.keys():
			if k not in PERMITIDOS:
				raise ValueError(f"Denominación {k} no permitida")

	def __str__(self):
		return f"Caja {self.caja} total: {self._total()}"

	def _total(self):
		total = 0
		for billete, cantidad in self.caja.items():
			total += billete * cantidad
		return total

	def agregar(self, billetes):
		for billete in billetes.keys():
			if billete in PERMITIDOS:
				self.caja[billete] = self.caja.get(billete,0) + billetes[billete]
			else:
				raise ValueError(f"Denominación {billete} no permitida")

	def quitar(self, billetes):
		for billete in billetes.keys():
			if billete in PERMITIDOS:
				try:
					if self.caja[billete] < billetes[billete]:
						raise ValueError(f"No hay suficientes billetes de {billete}")
					self.caja[billete] -= billetes[billete]
					
				except KeyError:
					raise ValueError(f"No hay billetes de {billete}")
			else:
				raise ValueError(f"Denominación {billete} no permitida")

#for clave in list(d.keys())


