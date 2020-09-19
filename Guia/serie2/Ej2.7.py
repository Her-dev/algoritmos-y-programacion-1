def domino ():
    """imporime por pantalla las fichas del domino"""
    for i in range (7):
        for x in range (i+1):
            print(i,"|",x)

domino()
