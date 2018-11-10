d = {"john pual":9959,"michel john":9618,"teresa":4455}
w = input('name of the worker is ')
l = list(d.keys())
for i in l:
	if w in i:
	 print(i,' : ',d[i])
	
