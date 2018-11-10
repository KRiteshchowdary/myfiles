s = input()
a = s.split()
S = int(a[0])
X = int(a[1])
N = int(a[2])
T = []
Y = []
count = 0
sum =0
for i in range(0,N):
	ss = input()
	aa = ss.split()
	T.append(int(aa[0]))
	Y.append(int(aa[1]))
for j in range(0,N):
	while (sum<S):
		if i//T[j] == 1:
			sum= sum+Y[j]
			count=count+1
		else:
			sum = sum + X
			count = count+1
print(count)
	
	
