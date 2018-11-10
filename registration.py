import re 
n = input('Registration number is ')
if re.match("^[1-9][0-9][Bb][Cc][eE][0-9][0-9][0-9][0-9]$",n):
	print('Registration number correct.CSE student')
elif re.match("^[1-9][0-9][Bb][Ii][Tt][0-9][0-9][0-9][0-9]$",n):
	print('Registration number correct.IT student')
else:
	print('Registration number incorrect.')


m = int(input())
if re.match("[1][1][1][1][1][1]",m):
    print("Bad")
elif re.match("[0][0][0][0][0][0]",m):
    print("Bad")
else:
    print("Good")
