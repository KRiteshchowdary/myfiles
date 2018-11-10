import re
p = input("Your Pancard number is ")
if re.match("^[A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][A-Z]$",p):
	print('Pancard number valid.')
	m = input('Your ACCOUNT  number is ')
	if re.match("^[6][0][7][3][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$",m):
		print('Card number verrified.')
		a = input("your aadhar card number is ")
		if re.match("^[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$",a):
			print('Aadhar card verified and linked.')
		else:
			print('Incorrect Aadhar card.')
	else:
		print('Incorect card number.')
else:
	print('Pan card number invalid.')

