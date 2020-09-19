from math import sqrt 

def min_max_poli2(a,b,c):
	"""Dado los coeficientes a,c,c de un polinomio de segundo grado, devuelve el mínimo y máximo"""
	if a > 0:
		print ("Es mínimo")
		return (-b/(2*a))
	print ("Es máximo")
	return (-b/(2*a))

def raices(a,b,c):
	"""Dedo los coeficientes a,b y c de un polinomio de segundo grado, devuelve sus raices"""
	if a:
		if (b**2 - 4*a*c) >= 0:
			raiz1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
			raiz2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
			
			return raiz1, raiz2
		
		raiz1 = (-b + 1j* sqrt(-1 * (b**2 - 4*a*c))) / (2*a)
		raiz2 = (-b - 1j* sqrt(-1 * (b**2 - 4*a*c))) / (2*a)

		return raiz1, raiz2

	print ("No ingresó un polinomio de grado 2")

def inter_rectas(m1,y1,m2,y2):
	"""Dado las pendientes y ordenadas al origen de dos rectas m1,y1,m2.y2, devuelve su intersección"""
	if m1 or m2:
		if m1 != m2:
			xint = (y2-y1) / (m1 - m2)
			yint = y1 + xint * m1

			return xint, yint

		elif y1 == y2:
			print ("son las mismas rectas")

		else:
			print("no hay intersección")
	elif y1 == y2:
		print("Son la misma constante")
	else:
		print("No exite intersección")









