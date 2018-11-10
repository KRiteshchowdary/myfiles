#To find  the digit factors of the given number.
#EX-for 256 the digits are 2,5,6 and only 2 is divides 256 so print only 2.
n = int(input("Enter number "))
l = []
a = n
while n>0:
	l.append(n%10)
	n = n//10
count = 0
for i in l:
	if a%i==0:
		count = count+1
		print(i)
if count == 0:
	print("No ditit factors for given number.")
