class Brazo:
	def __init__(self, area, aguante):
		self.area = area
		self.aguante = aguante

class Tatuaje:
	def __init__(self, nombre, area, dolor):
		self.nombre = nombre
		self.area = area
		self.dolor = dolor

class Tatuador:
	def __init__(self, nombre):
		self.nombre = nombre
		self.tatuajes = 0

	def tatuar(self, brazo, tatuaje):
		if tatuaje.dolor > brazo.aguante:
			raise ValueError("No te lo vas a bancar")
		if tatuaje.area > brazo.area:
			raise ValueError("Ya no te queda mas lugar")

		brazo.area -= tatuaje.area
		self.tatuajes += 1

	def __repr__(self):
		return f"{self.nombre}: {self.tatuajes} tatuajes realizados"