'''
Error HAndling -> 

syntax errors

logical error = 2 + 2 = 4
22

runtime error 

try:
    //statements we need to check
except <exception_error>:
    //except statements
else:
    //else statement will get executed only if there is no exception
finally:
    //no matter what , it will get executed

'''

num1 = 5
num2 = 0

try:
     print(num1/num2)
     # print(a)
except ZeroDivisionError as e:
     print(e)
     print("Denominator cannot be zero")
except BaseException as e:
     print(e)

try:
     #file = open("./abc.txt","r")
      file = open("./temp.txt","r")
except FileNotFoundError as e:
     print(e)
else:
     print("Else part")
     file.close()
finally:
     print("Finally block")

print("Other lines of code")


name=input("Enter your name: ")

if name.isnumeric():
     raise Exception ("Numbers not allowed")
print("Welcome! ", name)


def func():
     try:
         print("1")
     except:
         print("2")
def func():
     try:
         print("1")
     except:
         print("2")
     else:
         print("3")
     finally:
         print("4")
def func2():
     try:
         return("1")
     except:
         return("2")
     else:
         return("3")
     finally:
         return("4")

func()
print(func2())