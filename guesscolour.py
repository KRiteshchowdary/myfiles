import random
colours = ["red","green","blue","yellow","white","grey"]
colour = random.choice(colours)
co = input("Enter colour ")
if co == colour:
	print("Colour matched.")
else:
	print("Colour not matched.")
print("Actual colour is ",colour,".")
