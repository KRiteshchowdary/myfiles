import re
s = input('Your string is ')
x = input('Word to find in the given string  is ')
if re.search(x,s):
	print('Word is  found in given string.')
else:
	print('Word not found in the given string.')
