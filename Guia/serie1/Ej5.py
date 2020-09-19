def operaciones(a,b):
    suma = a+b
    resta = a-b
    div = a/b
    mult = a*b

    print("la suma es ", suma, "la resta es ", resta, "la divición es ", div, "la multiplicación es ", mult)
operaciones(3,5)

def tablamult(n):

    print ("la tabla de multiplicar de ", n, "es: ")
    for i in range (11):
        print (i*n)

tablamult(9)
