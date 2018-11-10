dictionary = {"L"="lists","S"="sethots","T"="tuples","D"="dictionary"}

word = input("what's your word?")
 while (word in dictionary):
  print("dictionary[word]")
  break
else:
  print("word is not present")
    
