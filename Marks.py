a = float(input('Percntage in Maths  is '))
b = float(input('Percntage in Physics is '))
c = float(input('Percntage in EVS is '))
d = float(input('Percntage in CSE is '))
e = float(input('Percntage in English is '))
t = (a+b+c+d+e)/5
if (t >= 90):
	print("Grade is 'A' and percentage is ",t)
elif (t >= 85 and t < 90):
	print("Grade is 'B' and percentage is ",t)
elif (t >= 80 and t < 85):
	print("Grade is 'C' and percentage is ",t)
elif (t >= 75 and t < 80):
	print("Grade is 'D' and percentage is ",t)
elif (t >= 70 and t < 75):
	print("Grade is 'E3' and percentage is ",t)
elif (t < 70):
	print("Grade is 'F' and percentage is ",t)
