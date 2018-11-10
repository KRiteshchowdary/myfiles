s = input()
N = int(s.split()[0])
X = int(s.split()[1])
Y = int(s.split()[2])
ss = input()
l = ss.split()
count = 0
for i in range(0,N):
	if X>Y:
		if int(l[i])>=Y and int(l[i])<=X:
			count =  count+1
		else:
			continue
	else: 
		if int(l[i])>=X and int(l[i])<=Y:			
			count = count+1
		else:
			continue
if count == N:
    print("YES")
else:
    print("NO")
