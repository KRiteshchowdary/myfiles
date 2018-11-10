a = float(input('Basic pay  is   '))
b = float(input('Percntage of DA is  '))
c = float(input('Percntage of LA is  '))
d = float(input('Percntage of HRA is  '))
e = float(input('Percntage of TAX is  '))
f = float(input('Percntage of LOAN is  '))
BONUS = float(input('Bonus is  '))
reply = input("Do you live in city   Yes(Y)   No(N)  ")
B = a*b/100
C = a*c/100
D = a*d/100
TP = a + B + C + D + BONUS
E = TP*e/100
F = TP*f/100
NPY = TP - E - F + 2000
NP = TP - E - F
if (reply == "Y"):
	print('City allowance is 2000.')
	print('Your salary is ',NPY,)
elif (reply == "n"):
	print('You have no city allowance.')
	print('Your salary is ',NP,)
else:
	print('Your city allowance is not registered property.Please consult the authorities.')
	print('Your salary is',NP)
