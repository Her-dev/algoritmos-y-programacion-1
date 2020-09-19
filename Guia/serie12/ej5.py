class Materia:
	def __init__(self, codigo, nombre, creditos):
		self.codigo = codigo
		self.nombre = nombre
		self.creditos = creditos

class Carrera:
	def __init__(self, materias): #materias es una lista de elementos clase Materia
		self.materias = materias
		self.codigos = self._lista_codigos()
		self.aprobadas = []

	def aprobar(self, codigo, nota):
		if codigo not in self.codigos:
			raise ValueError(f"La materia {codigo} no es parte del plan de estudios")
		
		for materia in self.materias:
			if materia.codigo == codigo:
				materia.nota = nota
				self.aprobadas.append(materia)

	def __str__(self):
		#print(f"Créditos: {self._total_creditos()} -- Promedio: {self._promedio()} -- Materias aprobadas: ")
		#for materia in self.aprobadas:
		#	print(f"{materia.codigo} {materia.nombre} ({materia.nota})")
		#return ""

		string = f"Créditos: {self._total_creditos()} -- Promedio: {self._promedio()} -- Materias aprobadas: \n"
		for materia in self.aprobadas:
			string += f"{materia.codigo} {materia.nombre} ({materia.nota}) \n"

		return string.rstrip("\n")


	def _lista_codigos(self):
		codigos = []
		for materia in self.materias:
			codigos.append(materia.codigo)

		return codigos

	def _total_creditos(self):
		creditos = 0
		for materia in self.aprobadas:
			creditos += materia.creditos

		return creditos

	def _promedio(self):
		if not self.aprobadas:
			return "N/A"
		suma = 0
		for materia in self.aprobadas:
			suma += materia.nota

		return suma / len(self.aprobadas)




