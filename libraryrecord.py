#To record the names and time of entry and print when asked
n=[]
time =[]
v =5
while v >0:
	a=input("What is your name ")
	if a != "stop":
		n.append(a)
		time.append(input("time is"))
	else:
		break
		
a = input("Enter name to be searched ")
if a in n:
	n1 = n.index(a)
	print(a,"'s entry is found.")
	print(a," entered at ",time[n.index(a)],' .')
else:
	print("Entry of ",a," is not found.")
