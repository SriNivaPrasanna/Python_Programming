"""
DRY -> Donot Repeat Yourself

Loops -> To repeat

# for loop (for in loop)

# TODO:  while loop
# initialization
# condition 
# loop statements
# re-initialization (increment/decrement)


"""

# TODO: printing hello 5 times
'''
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
'''
# initialization
# i = 1

# # condition 
# while i <= 5:
#     # statement
#     print("Hello: ", i)

#     # re-initialization
#     i += 1

# print("After while loop")


# TODO: writing whether a given number in odd or even

# num = 0

# while num <= 10:
#     if num%2 == 0:
#         print(num, " is even")
#     else:
#         print(num, " is odd")
    
#     num+=1

# TODO: WAP to print reverse counting 

# num = 10

# while num >= 1:
#     print(num)
#     num = num - 1 


# TODO: for loop 
'''
It is applied on the iterables
list, tuple, dictionary, set, range

iterator
iterables -> these are the ones on which we can iterate
iteration -> looping 
'''

#fruits = ["mango", "orange", "banana", "guava"]

#for fruit in fruits:
#    print(fruit)

#for i in range(5):
#    print(i, end=" ")


# TODO: else in for loop
'''
else part of the loop will be executed only if 
loop is completely executed without any external termination
'''
'''
for i in range(5):
    print(i)
else:
   print("for loop else part")
   print("All elements are successfully executed")
'''

# TODO: WAP to print fiboannci series
'''
# 0 1 1 2 3 5 8 ......

a = 0
b = 1

print(a , end =" ")
print(b , end =" ")

for i in range(2, 10):
    c = a + b
    a = b
    b = c
    print(c, end=" ")


'''
# TODO: WAP for the factorial of a given num
# 5 = 5 *4 * 3 * 2 * 1 = 120
'''
num  = int(input("Enter the number: "))
fact =1 
for i in range(1 , num +1 ):
    fact = fact * i
    
    print("Factorial of" , num ,"is :" ,fact )

'''