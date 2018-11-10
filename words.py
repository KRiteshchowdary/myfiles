l = []
k = 9
count = 0
while k>0 :
	name = input('Name please ')
	if name != 'stop':
		l.append(name)
	else:
		break
for i in l:
	if len(i) > count:
		count = len(i)

