N = int(input())
num = []
for j in range(0,N):
	num.append(j)
print(num)
for i in num:
	if i%2==0:
		num[i] = N-i+1
		print(num[i])
	else:
		num.remove(i)
		N = len(num)
		
