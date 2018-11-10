s = input('your sring is ')
n = s.find('not')
p = s.find('poor')
b = s.find('bad')

if n == -1:
	print("'not' is not found in given string")
else:
	("not is first found in string at index ",s.find('not')
if p == -1:
	print("'poor' not found in given string")
else
	print('poor is first found at index',s.find('poor'))
if b == -1:
	print("'bad' not found in given string")
else
	print('bad is first found at index',s.find('bad'))
	
if b + 4 == p  and  b != -1:
	print(s.replace('bad', 'good'))
else:
	print('string doest have bad following poor')
