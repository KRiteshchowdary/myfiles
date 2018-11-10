n = int(input()) 
s1 = {1,2} - {1,2}
s2 = {1} - {1}
for i in range(0,n):
    l1 = input()
    l2 = input()
    for j in l1:
        s1.add(j)
    for k in l2:
        s2.add(k)
s =s1&s2
cost = len(s1)+len(s2)-2*len(s)
print(cost)
