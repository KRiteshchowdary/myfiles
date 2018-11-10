p = input('Your word is  ')
list_1 = ['q','w','e','r','t','y','u','i','o','p']
list_2 = ['a','s','d','f','g','h','j','k','l']
list_3 = ['z','x','c','v','b','n','m']
count = 0
count1 = 0
count2 = 0
for i in p:
	if i in list_1:
		count = count+1

if count == len(p):
	print('Yes word can be typed within a the 1st row.')
else:
	print("No it can't be typed within a the 1st row.")

for j in p:
	if j in list_2:
		count1 = count1+1

if count1 == len(p):
	print('Yes word can be typed within  the 2nd row.')
else:
	print("No it can't be typed within  the 2nd row.")
	
for k in p:
	if k in list_3:
		count = count+1

if count2 == len(p):
	print('Yes word can be typed within the 3rd row.')
else:
	print("No it can't be typed within the 3rd row.")
