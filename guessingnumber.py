import random 
n = int(input("Number of times you want to try "))
c =0
i = 0
while(i<n):
	num = int(input("Your guess "))
	num1 = random.randint(1,10)
	if num == num1:
		print("Your guess is correct")
		c = c+1
	else:
		print("your guess is incorrect")
	i = i+1

print("Probability of guessing correctly is ",c//n)
