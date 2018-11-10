l = []
n = input()
for i in n:
	l.append(i)
l1 = l
print(l)
print(l1)
a = len(l1)
while a>1:
	for i in range(1,a+1):
		a = len(l1)
		print(i)
		print(i%a == 0)
		print(l1)
		print(a)
		if i%a == 0 and i!= 0:
			print(l1)
		else:
			if a%2==0:
				print(l1)
				print(int((a)/2))
				l1.remove(l1[int((a)/2)])
				print(l1)
			else:
				print(int((a-1)/2))
				
				l1.remove(l1[int((a-1)/2)])
				print(l1[int((a-1)/2)])
				
				print(l1)

