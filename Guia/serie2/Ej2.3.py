def cel_faren(f):
    """Dado un valor en grados fahrenheit"""
    c=(f-32)*(5/9)
    return c


def tablafaren ():
    """Arma una tabla de conversión celsius y fahrenheit"""
    print ("Grados Fahrenheit |", "Grados Celsius")
    for f in range (0,121,10):
        c=cel_faren(f)

        print (f,"|",c)

tablafaren()
