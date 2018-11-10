a = int(input("number is  ")
int(b)=a%10
int(c)=(a%100 - d)/10
int(d)=a//100
if a<100:
	print('number is not armstrong number')
elif (b**3 + c**3 + d**3 == a):
	print('number is armstrong number')
else:
	print('number is not armstrong number')
