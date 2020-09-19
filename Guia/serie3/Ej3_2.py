from Ej3_1 import a_segundos
from Ej3_1 import de_segundos

def juntar ():
	"""Pide al usuario dos duraciones expresadas en hora, min, seg; las suma y devuelve el total en hora, min, seg"""
	h1 = int(input("Ingrese la cantidad de horas"))
	m1 = int(input("Ingrese la cantidad de minutos"))
	s1 = int(input("Ingrese la cantidad de segundos"))
	h2 = int(input("Ingrese la cantidad de horas"))
	m2 = int(input("Ingrese la cantidad de minutos"))
	s2 = int(input("Ingrese la cantidad de segundos"))

	seg = a_segundos(h1,m1,s1) + a_segundos(h2,m2,s2)

	print (de_segundos(seg))
	return de_segundos(seg)

juntar()

""" 
	seg = 0
    for i in range(n):
		h1 = int(input("Ingrese la cantidad de horas"))
		m1 = int(input("Ingrese la cantidad de minutos"))
		s1 = int(input("Ingrese la cantidad de segundos"))
		seg = seg + a_segundos(h1,m1,s1)