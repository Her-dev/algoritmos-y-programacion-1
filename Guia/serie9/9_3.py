def agenda():
	"""Va preguntando nombres y devuelve su telefono. permite cambios o guardar números nuevos"""
	agenda = {}

	while True:
		nombre = input("Ingrese el nombre (* para cerrar): ")

		if nombre == "*":
			break

		if nombre not in agenda:
			tel = input("No está en la agenda, ingrese su número (* para cerrar): ")
			
			if tel == "*":
				break

			agenda[nombre] = tel
			continue

		if input(f"El número es {agenda[nombre]}, desea corregirlo? [si/no]: ") == "si":
			agenda[nombre] = input("ingrese nuevo número: ")

agenda()


