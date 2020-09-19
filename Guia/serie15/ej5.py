def par(n):
	if n == 1:
		return False

	else:
		return not par(n - 1)

def impar(n):
	if n == 1:
		return True

	else:
		return not impar(n - 1)

print(par(9))
print(impar(9))
print(par(10))
print(impar(10))