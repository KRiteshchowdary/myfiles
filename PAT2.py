w = input('what is your word ')
l =[]
for i in w:
    n = w.count(i)
    l.append(n)
    
count = 0
for i in l:
    if i>1:
        count = count+1
if count > 0:
    print('Bad word')
else:
    print('Good word')
