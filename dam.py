n = int(input('Number of places from which water flows '))
d = float(input('Max capacity of water in dam in gallons is '))
l = []
for i in range(1,n+1):
	a = float(input('Gallons of water from canals are '))
	l.append(a)
	i = i+1
print('Water in the dam is ',sum(l),'gallons')

if sum(l) > d:
	r = sum(l)-d
	print('Dam is overlaoded open gates to realease ',r,'gallons.')
else:
	print('Dam not overloaded.Remaining amount of water that can be added is ',d-sum(l),'gallons.')
