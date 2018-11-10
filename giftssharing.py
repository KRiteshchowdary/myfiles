N = int(input("totla number of gifts"))
count = 0
for m in range(0,N):
	for a in range(0,N):
		for p in range(0,10):
			if m+a+p==10 and m>a and a>p:
				print(m, a, p)
				count = count+1
			else:
				continue
print("total number of ways are ",count)
