s = input("your string is ")
k = s.endswith('ing')
if (len( s ) <= 3):
	print('String too small')
elif (k == True):
	print(s + 'ly')
else:
	print(s + 'ing')
