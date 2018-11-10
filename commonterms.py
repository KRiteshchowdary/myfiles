s = {2,3,4}-{2,3,4}
S = int(input("number of items requested by son "))
for i in range (1,S+1):
	a = input('Item by son ')
	s.add(a)
d = {1} - {1}
D = int(input("number of items requested by daughter "))
for k in range(1,D+1):
	l = input('Item wanted by daughter')
	d.add(l)
		
c = s&d

print('Common items are ',c)

print('Son items are ',s-c)

print('Daughter items are ',d-c)

