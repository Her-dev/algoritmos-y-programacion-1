def pares():
    """Devuelve todos los números pares entre dos números que se ingresan por pantalla"""
    n1=int(input("Ingrese el primer número: "))
    n2=int(input("Ingrese el segundo número: "))

    for i in range(n1 + n1 % 2, n2+1, 2):
    	print (i)

pares()

   
        

