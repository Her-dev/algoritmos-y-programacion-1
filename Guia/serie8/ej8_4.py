def facturador(info, vendidos):
	"""Dada una lista "info" que consiste en (identicador, descripción, precio) y una lista
	de productos a facturar, imprime una factura que incluya la cantidad, la descripción, el precio unitario
	y el precio total de cada producto comprado, y al  nal imprima el total general."""
	total = 0

	for i in range(len(vendidos)):
		for j in range(len(info)):
			if vendidos[i][0] == info[j][0]: #Si el identificador de los productos a facturar es igual que el de la info
				print((vendidos[i][1], info[j][1], info[j][2], vendidos[i][1] * info[j][2]))
				total += vendidos[i][1] * info[j][2]

	print(f"El monto total es {total}")

facturador([(1,"es el buen fla",50), (2,"compralo que no te vas a arrepentir", 100), (3,"mi chorizo",1000)],[(1,10),(2,50),(1,20),(3,1)])
