l = [1,2,3,4,5,6,7]
r = input('Object to be found ')
count = 0
for i in range(0,len(l)+1):
	if l[i] != r:
		count = count+1
	else:
		break
	
print 'Requested object at position',count
