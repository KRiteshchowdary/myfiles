p = input('Your password is ')
import re
if len(p) <= 8:
	print('Password short')
elif re.match("^[^a-zA-Z]",p):
	print('Password must start with letter')
elif re.match("^[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]",p):
	print('Password must have atleast with a number and charecter')
else:
	print('Password ok')
