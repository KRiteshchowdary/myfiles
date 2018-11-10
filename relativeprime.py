n = int(input('Your first number is '))
m = int(input('Your second number is '))
l = []
count = 0 
count1 = 0
if n>m:
	for i in range (2,m+1):
		if m%i == 0:
			l.append(i)
else:
	for i in range (2,n+1):
		if n%i == 0:
			l.append(i)
for j in l:
	if n>m:
		if n%j == 0:
			count = count+1

	else:
		if m%j == 0:
			count1 = count1+1
	
		
			
if count>0 or count1>1:
	#print('Common term is ',j)
	print('They are not relatively prime')
else:
	print('Numbers are relatively prime')
