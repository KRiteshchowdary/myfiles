import random
num = random.uniform(1,6)
print("Give number greater than 6 if you want to quit")
num2 = int(input("Guessed number is "))
co = 0
count = 0
while(num2<7 and num2>0):
	if num == num2:
		print("Guess is correct.")
		count = count+1
	else:
		print("guess is incorrect")
		co = co +1
	num = random.uniform(1,6)
	num2 = int(input("Guessed number in die "))
total = count + co
print("Propability of guessing correctly ",count//total)
	
