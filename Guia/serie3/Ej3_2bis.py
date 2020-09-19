from Ej3_1 import a_segundos
from Ej3_1 import de_segundos

def juntar():
	"""Pide al usuario n duraciones expresadas en hora, min, seg; las suma y devuelve el resultado"""
	n = int(input("Ingrese la cantidad de intervalos de tiempo que quiere sumar: "))
	seg = 0
	for i in range(n):
		h = int(input("Ingrese la cantidad de horas: "))
		m = int(input("Ingrese la cantidad de minutos: "))
		s = int(input("Ingrese la cantidad de segundos: "))

		seg = seg + a_segundos(h,m,s)

	hms = de_segundos(seg)

	print (hms)

juntar()