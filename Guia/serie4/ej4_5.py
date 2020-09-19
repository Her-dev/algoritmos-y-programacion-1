def bisiesto(anio):
	"""Dado un año, devuelve True si es bisiesto y False si no lo es"""
	if (not anio % 4) and (anio % 100):
		return True

	elif (not anio % 100) and (not anio % 400):
		return True

	return False

def dias_mes(anio, mes):
	"""Dado un año y un mes, devuelve la candtidad de días de dicho mes"""
	if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
		return 31 

	elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
		return 30

	elif mes == 2:
		if bisiesto(anio):
			return 29
		return 28
	else:
		return False


def validar_fecha(anio,mes,dia):
	"""Dada una fecha (anio, mes, dia) devuelve True si es válida o False si no lo es"""
	if dia <= dias_mes(anio,mes): #Si se ingresa un valor de mes mayor (o menor) a 12, va a quedar dia <= False --> False, por lo que el programa funciona perfectamente.
		return True
	return False

def dias_faltantes_mes(anio,mes,dia):
	"""Dada una fecha, devuelve cuantos días faltan para terminar el mes"""
	if validar_fecha(anio,mes,dia):
		return (dias_mes(anio,mes) - dia)
	return False

def dias_faltantes_anio(anio,mes,dia):
	"""Dada una fecha, devuelve cuantos días faltan para terminar el año"""
	dias = dias_faltantes_mes (anio,mes,dia)
	for i in range(mes + 1, 13):
		dias += dias_mes(anio, i)
	return dias

def dias_transcurridos_anio_fecha(anio,mes,dia):
	"""Dada una fecha devuelve cuantos días del año transcurrieron hasta la fecha"""
	dias = dia 
	for i in range(1, mes):
		dias += dias_mes(anio,i)
	return dias 

def tiempo_entre_fechas(anio1,mes1,dia1,anio2,mes2,dia2):
	"""Dadas dos fechas (anio, mes, dia) devuelve el tiempo transcurrido entre ellas
	Se supondrá que la primera fecha es anterior a la segunda"""
	anio = anio2 - (anio1 + 1)
	mes = 12 - (mes1 + 1) + (mes2 - 1)
	dia = dias_faltantes_mes(anio1,mes1,dia1) + dia2

	if mes >= 12:
		mes = mes - 12 
		anio = anio + 1

	return dia, mes, anio
	
print (tiempo_entre_fechas(2000,1,1,2020,1,1)