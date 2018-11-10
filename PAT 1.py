d = int(input('How many days do you want to take the car for rent '))
k = int(input('How many killometers is your journey distance '))
cost1 = 1500 + k*9
cost2 = d*4000 
if cost1>cost2:
	print('plan 2 is best for your journey.')
	print('Plan 2 costs RS',cost1,'only.')
elif cost1<cost2:
	print('Plan 1 is best for your journey.')
	print('plan 1 costs RS',cost2,'only.')
else:
	print('Any plan is good for your journey.')
	print('Plan 1 and Plan 2 costs RS',cost1,'only.')
