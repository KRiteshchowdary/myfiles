n = int(input())
ss = input()
s = ss.split()
power = int(s[2])
x = int(s[0])
y = int(s[1])
for i in range(0,n):
	print(" \n")
	for j in range(0,n):
			if i == x and j == y:
				print(power,end = " ")
			else:
				for k in range(0,power):
					if x-i == k and y-j == k:
						print(power-k)
					elif x-i == k or y-j == k:
						print(power-k)
					elif x+i == k and y+j == k:
						print(power-k)
					elif x+i == k or y+j == k:
						print(power-k)
					else:
						continue
