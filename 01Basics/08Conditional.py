'''
Conditionals: We are going control the flow of statements on the basis of the provided condition

NOTE: indentation -> extra white space which defines the block in Python

only if

if condtion:
    if statements

##########################
    
if else pair

if condition:
    if statements
else:
    else statements

#########################
    
if elif ladder
if condition:
    if statements
elif condition:
    elif statement
elif condition:
    elif statement
    .
    .
    .
    .
    .
else:
    else statements
'''
'''

weather = "rain"

weather = input("Please enter the weather: ")

if weather == "rain":
     print("Take the umbrella")

if weather == "rain":
    print("Take the umbrella")
else:
    print("Do not take umbrella")

print("other lines of code")
'''
# if weather == "summer":
#     print("It's summer!")
# elif weather == "winter":
#     print("It's winter!")
# elif weather == "rainy":
#     print("It's raining!")
# else:
#     print("Enter the correct weather")


# if weather == "summer":
#     print("It's summer!")
# if weather == "winter":
#     print("It's winter!")
# if weather == "rainy":
#     print("It's raining!")
# else:
#     print("Not raining")






# whether a person can have a licence
'''
age = int(input("Please enter your age: "))

if age >= 18:
    print("You can have licence")
else:
    print("You cannot have the licence")
'''
# WAP to find whether the given number is +ve, -ve or 0
'''
num = int(input("Enter a num: "))

if num == 0:
    print("Zero")
elif num > 0:
  print("Positive")
elif num < 0 :
  print("Negative")
else:
    print("Enter a valid num")
'''

# TODO: WAP to find whether program is odd/even
'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("number is even")
else:
    print("Num is odd")
'''

# TODO: Nested if else
'''
if :
    if: 
        #if statement
    else:
        #else statement
else:
    if:
        #if statement
    
    else:
        #else statement

'''
'''
num1 = 34
num2 = 23
num3 = 12

if num1 >= num2:
    if num1 >= num3:
        print("Num1 is greatest: ",num1)
    else:
        print("Num3 is greatest: ",num3)
else:
    if num2 >= num3:
      print("Num2 is greatest: ",num2)
    else:
       print("Num3 is greatest: ",num3)

'''
'''
if num1 >= num2 and num1 >= num3:
   print("Num1 is greatest")
elif num2 >= num1 and num2 >= num3:
   print("Num2 is greatest")
elif num3 >= num2 and num3 >= num1:
   print("Num3 is greatest")
'''


# To login a user should use anyone method
'''
isEmail = False
isGoogle = False
isFacebook = True

if isEmail:
    print("You are logged in")
elif isGoogle:
    print("You are logged in ")
elif isFacebook:
    print("You are logged in")
else:
   print("Please login")
'''
# TO make an online purchase
'''
isLogin = True
isCard = True
isCart = True

if isLogin:
     if isCart:
         if isCard:
             print("Order placed successfully!")
         else:
             print("Enter valid card details")
     else:
         print("Add items in the cart")
else:
     print("Please login to place an order")
'''     



# TODO: WAP to implement a grading system
"""
marks should not be lesser than 0 and greater than 100
90-100 : A+
80 - 89 : A
"""

#TODO: Rating system 1 - 5
"""
rating should not be lesser than 1 or greater than 5
5 -> Amazing work
4 -> Keep it up
3 -> Good work
2 -> Can do better
1 -> Need to take care
"""
Rating = int(input("Enter the Rating for a Performence of the Work :"))

if Rating  <=1  &  Rating >=5 :
     if Rating == 1 :
             print("Need to take care")
     elif Rating == 2:
             print("Can do better")
     elif Rating == 3:
         print("Good Work")
     elif Rating == 4:
        print("Keep it up")
     elif Rating == 5:
        print("Amazing work")
     else :
        print("Enter the valid number")  
else:
     print("Enter the valid number")