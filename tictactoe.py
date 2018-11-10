for i in range(0,7):
	if i%2 == 0:
		print("---  ---  ---")
	else:
		print("| |  | |  | |")
print(" 1,2,3 positions of each row as 1 for player 1 and 2 for player 2  0 for unoccupied places")
i1= input()
r1 = i1.split()
i2 = input()
r2 = i2.split()
i3 = input()
r3 = i3.split()
for i in range(0,3):
	if (int(r1[i]) == int(r2[i])) and (int(r3[i]) == int(r1[i])):
		if r1[i] == 1:
			print("Player one wins")
		elif r1[i] == 2:
			print("player two wins")
		else:
			print("No one wins")
	elif r1[0] == r1[1] and r1[0] == r1[2]:
		if r1[1] == 1:
			print("Player one wins")
		elif r1[1] == 2:
			print("player two wins")
		else:
			print("No one wins")
	elif r2[0] == r2[2] and r2[1] == r2[0]:
		if r2[1] == 1:
			print("Player one wins")
		elif r2[1] == 2:
			print("player two wins")
		else:
			print("No one wins")
	elif r3[0] == r3[2] and r3[1] == r3[0]:
		if r3[1] == 1:
			print("Player one wins")
		elif r3[1] == 2:
			print("player two wins")
		else:
			print("No one wins")
			
	else:
		print("No one wins") 
	i = i+1

	
