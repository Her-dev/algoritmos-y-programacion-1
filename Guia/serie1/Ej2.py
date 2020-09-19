def rectanguloA (a,b):
    per= 2*a + 2*b
    print(per)
    return per

rectanguloA (2,1)

def rectanguloB (a,b):
    area=a*b
    print(area)
    return area

rectanguloB(5,5)

def rectmov (x1,x2,y1,y2):
    x= abs(x2-x1)
    y= abs(y2-y1)
    area= x*y
    print (area)
    return area
rectmov(3,8,20,25)

def percirc (r):
    per= 2*3.14159*r
    print (per)

percirc(2)

def arcirc (r):
    ar=3.14159*r**2
    print (ar)

arcirc (2)

def volesf (r):
    vol= (4/3)*3.14159*r**3
    print (vol)

volesf (3)
