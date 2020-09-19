def sep_entre_miles(cadena):
	"""reciba una cadena que contiene un largo número entero
	 y devuelva una cadena con el número y las separaciones de miles"""
	cadena_final = ""
	 
	for i in range(-1, -len(cadena) -1 , -1):
		cadena_final += cadena[i]

		if i % 3 == 0:
	 		cadena_final += "."

	return cadena_final[ : : -1]

print(sep_entre_miles("1500354353454"))


	 	


