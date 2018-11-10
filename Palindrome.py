a = int(input("number is  "))
b = a%10
c =(a%100 - b)/10
d = a//100
if (a  == b*100 + c*10 + d ):
	print('number is a palindrome')
else:
	print('number is not a palindrome')
	
