import math
n = int(input())
for i in range(0,n):
	s = input()
	a = s.split()
	for number in range(int(a[0]),int(a[1])+1):
		max = math.sqrt(number)
		
		if number % 2 == 0:
			print ("not prime number")
		else:
			for divisor in range(3,1 + int(max)):    
				if number % divisor == 0:
					print("not prime number")
				else:
					print("prime number")
