i=0
for i in range(2):
 word1 = raw_input("word 1 please  ")
 word2 = raw_input("word 2 please  ")
 
 n = int(word1.count(word2))

 if (word2 in word1):
     print("word found " + str(n) + (" times"))
 else:
     print("word not found")   
 i = i+1

