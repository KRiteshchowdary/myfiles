n1 = int(input("n1 "))
n2 = int(input("n2 ")) 
oper = input('operation please- ')

if(type(n1) is int and type(n2) is int):
 if oper in['+',"a"]:
   print(n1 + n2) 
  
 elif oper in ['-',"b"]:
   print(n1 - n2)
  
 elif oper in ['*','c']:
   print(n1 * n2)
 elif ((n2!=0) and oper in ['/','d']):
   print(float(n1) / n2 )
  
 else:
   print("this operation with n2 = 0 is not defined ") 
