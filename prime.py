import math
number = int(input("number  "))
max = math.floor(math.sqrt(number))

if number == 1:
    print ("It's a UNIT.It's neither prime nor composite.")
elif number == 2:
    print ("It's a PRIME number and a even number.")

elif number % 2 == 0:
    print ("It's a COMPOSITE number and a even number.")
else:
    for divisor in range(3,1 + int(max)):    
        if number % divisor == 0:
            print ("It's a COMPOSITE and a odd number ." )
        else:
            print ("It's a PRIME number and a odd number.")
