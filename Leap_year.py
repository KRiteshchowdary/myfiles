y = int(input('what year is it  '))
if y%4  == 0 and y%100 != 0 or y%400 == 0:
	print("It's a leap year.")
else:
	print("It's not a leap year.")
