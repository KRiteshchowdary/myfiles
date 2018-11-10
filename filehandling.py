class Person:
 def __init__(self, name, age):
    self.name = name
    self.age = age

 def setGender(self, gender):
      self.gender = gender
vinay = Person("Vinay", 17)
vinay.setGender("Male")

ajay = Person("ajay", 17)
ajay.setGender("Male")
print("hello my name is " + ajay.name + ",my age is " +  str(ajay.age)+ " and my gender is "+ ajay.gender)
 