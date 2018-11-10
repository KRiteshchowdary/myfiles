e = []
o = []
n = int(input('How many number do you want to count odd and even '))
for i in range(1,n+1):
	if i%2 == 0:
		e.append(i)
	else:
		o.append(i)
	i = i+1
print('Odd number upto',n,'are ')
print(o)
print('Even numbers upto',n,'are ')
print(e)
