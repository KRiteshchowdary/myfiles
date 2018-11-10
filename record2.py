n = int(input("Number of students "))
N = []
M = []
P = []
C = []
for i in range(0,n):
	N.append(input("Name of student is "))
	M.append(int(input("Maths marks are ")))
	P.append(int(input("Physics marks are ")))
	C.append(int(input("Chemistry marks  are ")))
f = int(input("Fail mark is "))
m = int(sum(M))//n
p = int(sum(P))//n
c = int(sum(C))//n
t = m+p+c//3
print("Average of maths marks are ",m,".")
print("Average of physics marks are ",p,".")	
print("Average of chemistry marks are ",c,".")
print("Total average  marks are ",t)
print("Maximum maths marks are ",max(M)," and are scored by ",N[M.index(max(M))],".")
print("Maximum physics marks are ",max(P)," and are scored by ",N[P.index(max(P))],".")
print("Maximum chemistry marks are ",max(C)," and are scored by ",N[C.index(max(C))],".")
for i  in range(0,n):
	a = (M[i] + P[i] + C[i])//n
	print("The average of ",N[i]," is ",a,".")
for i in range(0,n):
	if (M[i] + P[i] + C[i])//n < t:
		print(N[i]," has average that is  less than class average.")
	else:
		print(N[i]," has average that is more than class average.")
for i in range(0,n):
	if (M[i] + P[i] + C[i])//n < f:
		print(N[i]," has failed in  the exam.")
	else:
		print(N[i]," has cleared the exam.")

