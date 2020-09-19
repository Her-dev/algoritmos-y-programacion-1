def triangulares ():
    """Dado un número n ingresado por el usuario, devuelve los primeros n números triangulares"""
    n=int(input("Ingrese el número n hasta el cual quiere calcular los números triangulares: "))
    
    triang=0
    for i in range (n+1):
        triang = triang + i
        print (i, "-", triang)

triangulares()

def triangulares1 ():
    """Dado un número n ingresado por el usuario, devuelve los primeros n números triangulares cualculados por definición"""
    n=int(input("Ingrese el número n hasta el cual quiere calcular los números triangulares: "))
    
    for i in range (n+1):
        triang = (i*(i+1))/2
        print (i, "-", triang)

triangulares1()
