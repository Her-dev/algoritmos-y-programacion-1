def dias_numero_a_string(n):
	"""Dado un numero de día (1 a 366) y asumiendo que el año arrancó un lunes, devuelva que día de la semana es"""
	if n % 7 == 1:
		return "lunes"
	elif n % 7 == 2:
		return "martes" #elif conviene porque SOLO evalua si la condición anterior es falsa, por lo que me ahorro de avaluar bastantes condiciones
	elif n % 7 == 3:
		return "miercoles"
	elif n % 7 == 4:
		return "jueves"
	elif n % 7 == 5:
		return "viernes"
	elif n % 7 == 6:
		return "sabado"
	elif n % 7 == 0:
		return "domingo"

