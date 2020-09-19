def es_nota_decimal(digito, natural):
	"""Recibe un número decimal y uno natural, y decide se el primero se puede escribir como notación decimal del otro"""
	while digito < (natural + 1): #El "+ 1" va para que cuando el dígito se hace igual al natural, entre igual al while
		if digito == natural:
			return True

		digito = digito*10

	return False


