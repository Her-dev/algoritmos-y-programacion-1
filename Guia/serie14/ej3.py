from colas_pilas import Cola

def promedio_espera(llegadas):
	cola_bondi = Cola()
	tiempo = 0
	cantidad = 0

	for evento in llegadas:
		if evento[1] == "p":
			cola_bondi.encolar(evento)
			cantidad += 1

		elif evento[1] == "c":
			for lugares_libres in range(evento[2]): #evento[2] es la cantidad de lugares libres en el colectivo
				persona = cola_bondi.desencolar()
				tiempo += (evento[0] - persona[0]) #sumo la diferencia entre la llegada del bondi y el momento en el que llega 

	return tiempo / cantidad

print(promedio_espera([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)]))
