#1

# class Student:
        # def __init__(self,name,roll_no):
                # self.name = name
                # self.roll= roll_no
        # def display_details(self):
                # print('Student Name: ',self.name)
                # print('Roll No: ',self.roll)
# s1= Student('Darsana',101)
# s1.display_details()

#2

# class Employee:
#         def __init__(self,name,salary):
#                 self.name=name
#                 self.salary= salary
#         def display(self):
#                 return f'Employee : {self.name} | Salary : {self.salary}'
# emp= Employee('Aswathy',25000)
# print(emp.display())


#3

# class BankAccount:
#         def __init__(self,bal):
#                 self.bal=bal
#         def deposit(self,amt):
#                 self.bal=self.bal+amt
#                 print('Amount deposited: ',amt)
#                 print("Current balance: ",self.bal)
#         def withdraw(self,amt_withdraw):
#                 self.bal=self.bal-amt_withdraw
#                 print('Amount deposited: ',amt_withdraw)
#                 print("Current balance: ",self.bal)
# bank= BankAccount(50000)
# bank.deposit(2500)
# bank.withdraw(4500)


#4

# class User:
#         def __init__(self,name,password):
#                 self.name=name
#                 self.__pass=password
#         def display(self):
#                 print("Name:",self.name)
#                 print(self.__pass,'Password updated successfully')
# user1= User('Harsha',123)
# user1.display()

#5
class Product:
        def __init__(self,prod_name,price):
                self.name=prod_name
                self.price=price
        def discounted_Price(self,discount_rate):
                after_discount= self.price*(100-discount_rate)/100
                print('After discount the Product price is: ',after_discount)
biscuit= Product('Oreo',30)
biscuit.discounted_Price(50)
