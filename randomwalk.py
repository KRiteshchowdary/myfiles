import random
x = 0
y = 0
X = [1,-1]
Y = [1,-1]

n = int(input("Number of steps to take "))
for i in range(0,n):
	Xi = random.choice(X)
	Yi = random.choice(Y)
	if Xi == 1:
		print("One step towards East")
	else:
		print("One step towards West")
	
	if Yi == 1:
		print("One step towards North")
	else:
		print("One step towards South")
		
	x = x+random.choice(X)
	y = y+random.choice(Y)
print("Final position is (",x,",",y,")")
