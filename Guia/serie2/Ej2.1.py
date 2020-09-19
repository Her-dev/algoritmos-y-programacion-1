def capital():
    c=int(input("ingrese su capital inicial: "))
    i=int(input("ingrese la tasa de interés disponible: "))
    n=int(input("ingrese la cantidad de años que invertirá su capital: "))
    cn=c*((1+i/100)**n)
    print ("su capital final será de: ", cn, "pesos")

capital()
