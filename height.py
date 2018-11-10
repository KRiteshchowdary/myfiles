feet = int(raw_input("your feet please ? "))
inches = int(raw_input("your inches please ? ")) 

def func(feet,inches):
  feet_cm =feet * 12 * 2.54
  inches_cm = inches*2.54
  
  return feet_cm + inches_cm

class height:
 def __init__(self,feet,inches):
  self.feet = int(feet)
  self.inches = int(inches)
  self.cm =func(self.feet, self.inches)

test = height(feet,inches)
print 'i am ' + str(test.feet),str(test.in)
