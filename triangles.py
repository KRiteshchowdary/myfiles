a = int(raw_input("the length of a is: "))
b = int(raw_input("the length of b is: "))
c = int(raw_input("the length of c is: "))

if (a!=b and b!=c and c!=a):
 print( "its a scalene triangle ")
elif (a=b and b=c and c=a):
 print( "its a equaleteral triangle" )
else:
 print( "its a isossceles triangle" )
