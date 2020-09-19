def multiplica(x,y):
	return x * y

def mayor_producto(x1,x2,x3,x4):
	p1 = multiplica(x1,x2)
	p2 = multiplica(x1,x3) 
	p3 = multiplica(x1,x4)
	p4 = multiplica(x2,x3)
	p5 = multiplica(x2,x4)
	p6 = multiplica(x3,x4)

	return max (p1,p2,p3,p4,p5,p6)

print (mayor_producto(1,5,-4,-2))
print (mayor_producto(2,10,-7,-5))


