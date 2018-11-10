a = float(input('number 1 is  '))
function = input('desired function is  ')
b = float(input('number 2 is  '))

if (function == '+'):
	print(a + b)
elif (function == '-'):
	print(a - b)
elif (function == '*'):
	print(a*b)
elif (function == '/' and b != 0):
	print(a/b)
elif (function == '/' and b==0):
	print('b cannot be equal to zero')
else:
	print('give proper functions')
	
