def factorial (n):
    """Dado un numero n, calcula su factorial"""
    fact = 1
    for i in range (1,n+1):
        fact = fact*i
    return fact

def fact_m ():
    """Dado m números ingresados por el usuario, les calcula su factorial"""
    m=int(input("ingrese la cantidad de números a los cuales quiere calcular su factorial"))
    for i in range (m):
        n=int(input("ingrese un número a calcular su factorial"))
        fact = factorial(n)
        print (i, "|", fact)
fact_m()
    
        
