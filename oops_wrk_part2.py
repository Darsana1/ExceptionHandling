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





















































































































































































































































































































































































































































