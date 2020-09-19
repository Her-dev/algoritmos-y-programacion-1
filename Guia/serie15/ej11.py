def triangulo_pascal(n, k):
	if k == 0 or n == k:
		return 1

	else:
		return triangulo_pascal(n - 1, k - 1) + triangulo_pascal(n - 1, k)

print(triangulo_pascal(6,2))