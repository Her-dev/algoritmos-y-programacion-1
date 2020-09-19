from colas_pilas import Cola

class Impresora:
	def __init__(self, nombre, capacidad):
		self.nombre = nombre
		self.capacidad = capacidad
		self.cola = Cola()
		self.en_cola = 0

	def encolar(self, archivo):
		self.cola.encolar(archivo)
		self.en_cola += 1

	def imprimir(self):
		if self.cola.esta_vacia():
			return "No hay archivos encolados"

		elif self.capacidad == 0:
			return "No hay tinta :("

		else:
			self.capacidad -= 1
			self.en_cola -= 1
			return f"{self.cola.desencolar()} impreso"

	def cargar_tinta(self):
		self.capacidad += 1

class Oficina:
	def __init__(self):
		self.impresoras = {}

	def agregar_impresora(self, impresora):
		self.impresoras[impresora.nombre] = impresora

	def quitar_impresora(self, nombre):
		self.impresoras.pop(nombre)

	def impresora(self, nombre):
		return self.impresoras[nombre]

	def obtener_impresoras_libres(self):

		for impre in self.impresoras:
			






