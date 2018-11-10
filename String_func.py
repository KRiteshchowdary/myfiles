s = input('what is your string   ')
ss = input('what is your sub string   ')
v = ['i','e','o','u','a']
vowels = 0
print('no of spaces are ',s.count(' '))
print('total characters are',len( s ))
if ss not in s:
	print('Given sub string not in string.')
else:
	print('total no of times substring in string is',s.count( ss ))
print(s.capitalize( ))
print(s.upper())
print(s.lower())
for i in s:
	if i in v:
		vowels =vowels + 1
print('numbers of vowels in given string are ',vowels)
		


