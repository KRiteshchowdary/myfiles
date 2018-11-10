input1 = list(raw_input("list_1 :- ")) 
input2 = list(raw_input("list_2 :- "))

n = raw_input("clockwise shift by  ")

if(input1[0] == input2[int(n)]):
    print("lists similar")
else:
    print("lists diferent")    
