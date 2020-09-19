def numero_triangular(n):
	"""Calcula el n-esimo número triangular"""
	if n == 1:
		return 1

	else:
		return n + numero_triangular(n - 1)


