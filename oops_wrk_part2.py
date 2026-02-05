#6 Count object created
# class Car:
        # count=0
        # def __init__(self):
                # Car.count=Car.count+1
                
# c=Car()
# d=Car()
# c2=Car()
# c3=Car()
# print(Car.count)

# #7Default constructor
# class College:
#         def __init__(self,college_name='Unknown'):
#                 self.col_name=college_name
#         def display(self):
#                 print("college name: ",self.col_name)
# cl=College('Gec')
# c2=College()
# cl.display()
# c2.display()

#8 getattr

# class Book:
#         def __init__(self,book_name,author):
#                 self.book_name=book_name
#                 self.author=author
# b1=Book("wing of fire","Apj")
# print("Book_name:",getattr(b1,'book_name'))
# print("Book Author name:",getattr(b1,'author'))

#9 hasattr
# class Book:
#         def __init__(self,book_name,size):
#                 self.book_name=book_name
#                 self.size=size
# b1=Book("wing of fire","5MB")
# print(hasattr(b1,'size'))

#10 setattr

# class College:
#         def __init__(self,college_name):
#                 self.col_name=college_name
# c=College('Gec')
# print('Before update college namer : ',c.col_name)
# setattr(c,'col_name','Govt. Eng College,pkd')
# print('College Name is updated to: ',c.col_name)


#11 delattr
# class Book:
#         def __init__(self,bbok_no,book_name):
#                 self.no=bbok_no
#                 self.name=book_name
# b=Book('101','Python')
# delattr(b,'name')
# # print(b.name)
# print('Attribute Deleted')

#12 Single Inheritance
# class Person:
#         def __init__(self,compny):
#                 self.company_name=compny
# class Employee(Person):
#         def __init__(self, compny,emp_name):
#                 super().__init__(compny)
#                 self.name=emp_name
#         def display_emp_details(self):
#                 print('Employee Name: ',self.name)
#                 print('Company: ',self.company_name)
# emp= Employee('Infosys','Rahul')
# emp.display_emp_details()


#13 Multilevel
# class  Device:
#         def power_on(self):
#                 print("Device is powered on.")
# class Mobile(Device):
#         def call(self):
#                 print('Calling........')
# class SmartPhone(Mobile):
#         def connection(self):
#                 print('Internet Enabled..')
# vivo=SmartPhone()
# vivo.power_on()
# vivo.call()
# vivo.connection()

#14 Multiple Inheritance
# class Camera:
#         def take_photo(self,):
#                 print("Photo taken..")
# class MusicPlayer:
#         def play_music(self):
#                 print('Music Playing....')
# class Smartphone(Camera,MusicPlayer):
#         def show(self):
#                 print('Smartphone use camera and musicplayer')
# oppo= Smartphone()
# oppo.take_photo()
# oppo.play_music()
# oppo.show()


#15 MRO for multiple inheritance

# class A:
#     def method_a(self):
#         print("Method from A")

# class B:
#     def method_b(self):
#         print("Method from B")

# class C(A,B):
#     print('Method from C')

# ob = C()
# ob.method_a()
# ob.method_b()
# print(C.mro())

#16 super() to call parent
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         super().show()

# class C(A):
#     def show(self):
#         super().show()

# class D(B, C):
#     def show(self):
#         super().show()

# obj = D()
# obj.show()

#17
# class Shape:
#         def area(self):
#                 print('Different shapess.')
# class Circle(Shape):
#         def area(self):
#                 radius=4
#                 area=3.14*(radius**2)
#                 print("Area of circler: ",area)
# c=Circle()
# c.area()

#18super() inside overridden


# class Shape:
#         def area(self):
#                 print('Shape Drawn..')
# class Circle(Shape):
#         def area(self):
#                 super().area()
#                 print("Circle drawn")
# c=Circle()
# c.area()

#19 Hierarical inheritance
class Vehicle:
        def speed(self,speed):
                print('vehicle speed.')
class Car(Vehicle):
        def c_speed(self,car_speed):
                print('Car speed:',car_speed)
class Bike(Vehicle):
        def b_speed(self,bike_speed):
                print("Bike speed: ",bike_speed)
b=Bike()
c=Car()
c.c_speed(120)
b.b_speed(90)


#20 Hybrid Inheritance
class A:
        def method(self):
                print('Method A')
class B(A):
        def display(self):
                print("Display B")
class C(B,A):
        def show(self):
                print("Helooo")
                super().method()
c=C()
c.display()
c.method()
c.show()



































































































































































































































































































































































































































