#1
# num1=int(input("Enter first num: "))
# num2=int(input('Enter second num: '))
# try:
#         print(num1/num2)
# except ZeroDivisionError as z :
#         print(z)


#2
# try:
#         num=int(input('Enter num: '))
# except ValueError:
#         print('Invalid input.')
# print("checking....")
        
#3
# num=[9,89,56,2]
# try:
#         print(num[10])
# except IndexError:
#         print('List out of index range')

#4

# try:
#         open('oops1.py')
# except FileNotFoundError:
#         print('File doesnot exist')

# 5

# try:
#         num1=int(input("Enter first num: "))
#         num2=int(input("Enter second num: "))
#         print(num1/num2)
# except ValueError:
#         print('Invalid input')
# except ZeroDivisionError as z:
#         print(z)

# except:
#         print('Error handled successfully')

#6 use else block in try except
# try:
#         num1=int(input('Enter first num: '))
#         num2=int(input('Enter second num:'))
#         print(num1*num2)
# except ValueError:
#         print('Enter valid input.')
# else:
#         print("Multiplication completed successfully")

#7 using finally block

try:
        file=open('oops_wrk.py')
        print('File Opened')
except:
        print("File operation failed")
finally:
        print('file closed successfully')