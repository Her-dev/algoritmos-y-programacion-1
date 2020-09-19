def mcd_euclides(n,m):
	"""Dados dos números n y m, calcula su MCD"""

	while True:
		r = m % n
		if r == 0:
			break
		m = n
		n = r 

	print ("El MCD es: ", n)
	return n

mcd_euclides(60,48)
mcd_euclides(9,15)
mcd_euclides(15,9)
mcd_euclides(10,8)
mcd_euclides(12,6)