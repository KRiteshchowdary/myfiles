print('STUDENT 1')
a1 = input('what is your name ')
b1 = float(input('what is your mark in subject1 '))
c1 = float(input('what is your mark in subject2 '))
d1 = float(input('what is your mark in subject3 '))
l = []
l.append(a1)
l.append(b1)
l.append(c1)
l.append(d1)	
print("STUDENT 2")
a2 = input('what is your name ')
b2 = float(input('what is your mark in subject1 '))
c2 = float(input('what is your mark in subject2 '))
d2 = float(input('what is your mark in subject3 '))
m = []
m.append(a2)
m.append(b2)
m.append(c2)
m.append(d2)	
print('STUDENT 3')
a3 = input('what is your name ')
b3 = float(input('what is your mark in subject1 '))
c3 = float(input('what is your mark in subject2 '))
d3 = float(input('what is your mark in subject3 '))
n = []
n.append(a3)
n.append(b3)
n.append(c3)
n.append(d3)	

print(l)
A = (c1+d1+b1)/3
print('Average mark of ',a1,' is ',A)

B = (c2+d2+b2)/3

print('Average mark of ',a2,' is ',(d2+b2+c2)/3)

C = (c3+d3+b3)/3

print('Average mark of ',a3,' is ',(d3+b3+c3)/3)
 


D = (A+B+C)/3
print('Average of three students are ',D)
