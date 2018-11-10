m = int(input('Number M is '))
n = int(input('Number N is '))
if n>m:
	for i in range(2,m+1):
		if m%i == 0 and n%i == 0:
			print('numbers are coprime')
		else:
			print('numbers are not coprime')
elif n<m:
	for i in range(2,n+1):
		if m%i == 0 and n%i == 0:
			print('numbers are coprime')
		else:
			print('numbers are not coprime')
else:
	print('Numbers are coprime')
