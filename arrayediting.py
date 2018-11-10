s = input()
l= s.split()
n = int(l[1])
ss = input()
ar = ss.split()
su = 0
for i in range(0,n):
	sss = input()
	pro = sss.split()
	func = int(pro[0])
	a = int(pro[1])
	b = int(pro[2])
	
	if int(pro[0])==1:
		ar[a]=b
		print(ar)
	else :
		for i in range(a,b+1):
			su = su + int(ar[i])
		print(su )
