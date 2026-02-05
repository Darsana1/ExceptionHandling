#21 Polymorphism

# class Dog:
#         def sound(self):
#                 print("Dog barks...")
# class Cat:
#         def sound(self):
#                 print("Cat Meowsss.")
# d = Dog()
# c=Cat()
# d.sound()
# c.sound()

#22 Operator overloading
# class Distance:
#         def __init__(self,dist):
#                 self.km=dist
#         def __add__(self,other):
#                 return self.km + other.km
# d1=Distance(450)
# d2=Distance(100)
# print('Total distance: ',d1+d2)