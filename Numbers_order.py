a = float(input('a is '))
b = float(input('b is '))
c = float(input('c is '))
if(a>b and a>c):
	print('Greatest number is ',a)
elif(b>c and b>a):
	print('Greatest number is ',b)
elif(c>a and c>b):
	print('Greatest number is ',c)
else:
	print("numbers donot set well")
