def contrasenia():
	contra = "puchitahermosa"
	ingreso = " "
	
	while ingreso != contra:
		ingreso = input("Ingrese la contraseña: ")

	print ("TE AMOOOOOOOOOO")



def contrasenia_3intentos():
	contra = "puchitahermosa"
	ingreso = " "

	for i in range(3):
		ingreso = input("Ingrese la contraseña: ")

		if ingreso == contra:
			print("CORRECTO, TE AMO")
			break

		print ("Quedan ", 2 - i, "intentos")

from time import sleep

def contrasenia_3intentos_sleep():
	contra = "puchitahermosa"
	ingreso = " "

	for i in range(3):
		sleep(i*3)
		ingreso = input("Ingrese la contraseña: ")

		if ingreso == contra:
			print("CORRECTO, TE AMO")
			break

		print ("Quedan ", 2 - i, "intentos")
		

def contra_3int_sleep_bool():
	contra = "puchitahermosa"
	ingreso = " "

	for i in range(3):
		sleep(i*3)
		ingreso = input("Ingrese la contraseña: ")

		if ingreso == contra:
			print("CORRECTO, TE AMO")
			return True

		print ("Quedan ", 2 - i, "intentos")
	return False 

contra_3int_sleep_bool()



