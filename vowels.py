vowel = ['a','e','i','o','u','A','E','I','O','U']
word = input('What is your word? ')
count = 0
for i in vowel:
	if i in word:
		count = count+1
if count>0:
	print('Word has ',count,' vowels.')
else:
	print('Word does not have vowels.')

	
import re
		
if re.match("^[aeiouAEIOU]",word):
	print('An '+ word)
else:
	print('A '+ word)
	
