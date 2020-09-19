from colas_pilas import Cola

class TorreDeControl:
	def __init__(self):
		self.arribos = Cola()
		self.despegues = Cola()

	def nuevo_arribo(self, avion):
		self.arribos.encolar(avion)

	def nueva_partida(self, avion):
		self.despegues.encolar(avion)

	def ver_estado(self):
		arribo = ""
		despegue = ""
		for aviones in self.despegues:
			despegue += f"{aviones}, "
		despegue.rstrip(", ")

		for aviones in self.arribos:
			arribo += f"{aviones}, "
		arribo.rstrip(", ")

		return f"Vuelos esperando para Aterrizar: {arribo} \nVuelos esperando para Despegar: {despegue}"

	def asignar_pista(self):
		if self.arribos.esta_vacia():
			if self.despegues.esta_vacia():
				return f"No hay vuelos en espera"
			avion = self.despegues.desencolar()
			return f"El vuelo {avion} aterrizó con éxito."
		else:
			avion = self.arribos.desencolar()
			return f"El vuelo {avion} despegó con éxito."
		

