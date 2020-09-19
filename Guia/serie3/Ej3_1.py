def a_segundos(horas, minutos, segundos):
	"""Dado cantidad de horas, minutos y segundos; devuelve la cantidad en segundos"""
	return horas * 3600 + minutos * 60 + segundos



def de_segundos(segundos):
	"""Dado un intervalo en segundos, lo devuelve en horas, minutos y segundos"""
	horas = segundos // 3600
	minutos = (segundos % 3600) // 60
	seg = (segundos % 3600) % 60

	return horas, minutos, seg

