l =[]
d =1
u=0
for i in range (1,4):
 print('Marks of student',d,' are.')
 a = int(input('Subject1 '))
 b = int(input('Subject2 '))
 l.append(a)
 l.append(b)	
 d = d+1
for i in range(1,len(l)+1):
	if i <= 2:
		u+=(l[i])
		print('Student1 marks are ',u)
	elif i<5 and i>=3:
		u+=(l[i])
		print('Student1 marks are ',u)
	else:
		u+=(l[i])
		print('Student1 marks are ',u)
