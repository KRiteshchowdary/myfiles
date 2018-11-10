#ceaser ceapher
w = input("enter word ")
n = int(input("number"))
a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l =[]
s=[]
for i in w:
	l.append(i)
for j in l:
	n1 = a.index(j)
	n2 = (n1+n)%26
	s.append(a[n2])
for i in s:
	print(i,end="")
	
print(' ')

