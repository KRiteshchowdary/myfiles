for i in range(1,51):
	if i%3 == 0 and i%5 != 0:
		print('fizz')
	elif i%5== 0 and i%3 != 0:
		print('bizz')
	elif i%3 ==0 and i%5 == 0:
		print('fizzbizz')
	else:
		print(i)
