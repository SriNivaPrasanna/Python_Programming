'''
Operators -> It allows us to performn the operations

there are two types of operators
unary operator -> Only one operand is required

binary operators -> two operands are required
Arithmetic Opeators
Assignment Operators
Relational Operators
Logical Operators
Binary Operators

Membership Operator
Identity Operator
'''

# TODO: Unary Operators

#a = -2
#print(a)

# TODO: Binary Operators
# TODO: Assignment Operator '='
# NOTE: It assigns RHS literal value to LHS variable

#a = 5
#print(a)


# TODO: short hand notations
'''
x = 2
print("x before: ", x)
x = x + 3
x += 3

x = 2
#x = x * 5
x *= 5
print("x after: ", x)

'''
# TODO: Arithmetic Operators
'''
+ , - , / , *

** -> exponentation
% -> modulus (remainder)
// -> floor divison (providing integer quotient)
/ -> decimal quotient
'''
'''
num1 = 6
num2 = 3

print("Sum is :", num1+num2)
print("Subtraction ans is :", num1 - num2)
print("Multipliplication ans is :", num1 * num2)
print("Divison ans is:", num1/num2)

print("floor divison ans is :", num1 // num2)
print("Remainder is: ", num1%num2)

print("6 raise to the power 3 is: ", 6**3)

'''

# TODO: Relational operator
'''
It returns boolean value (True/False)

> : Greater than
< : Lesser than

NOTE: It will return True if either LHS value is greater/lesser than or equal to RHS value
>= : Greater than equal to
<= : Lesser than equal to


== : Equality
!= : Not equal to

'''
'''
num1 = 5
num2 = 2

print(num1 > num2)
print(3 > 7)
print(4 < 2)

print(5 >= 2)
print(5 >= 5)

# NOTE: '=' is assignment operator  whereas '==' is relational operator


print( 5 == 5)
# NOTE: It will prompt an error
#print(5 = 5)

print(5 != 5)
'''
# TODO: Logical Operators

'''
and : If anyone input is False output will be False

or : If anyone input is True output will be True

not : It reverses the state (makes True-> False)
'''
'''
print( 5>3 and 3>2)
print(2>3 and 5<8)


print(2>3 or 5<8)

# NOTE: Falsy -> False, 0, None ,''

print(not 0)
print(not -2)

# To login a user should use anyone method
isEmail = False
isGoogle = False
isFacebook = True

print(isEmail or isGoogle or isFacebook)


# TO make an online purchase
isLogin = True
isCard = True
isCart = True

print(isLogin and isCard and isCart)
'''
# TODO: Bitwise Operators
# These work on the bits

'''
| -> Bitwise or
& -> Bitwise and
^ -> Bitwise xor
<< -> Bitwise left shift
>> -> Bitwise right shift



print(5 | 15)
print(bin(15))

print(5 & 15)

print(5 ^ 15)

# << : It shifts the bit to the left side
# It increases the bits
# It multiplies

print(5 << 1)
print (5 << 2)


# >> : It shifts the bit to the right side
# It divides
# It decreases the number of bits

print(10 >> 1)

print(10 >> 2)
'''
'''
# TODO: Membership Operator (in)

nums = [23,45,34,21,67,36]

print(34 in nums)

print(4 in nums)
print(4 not in nums)
print(34 not in nums)
name = "John"

print("j" in name)
print("s" not in name)
print("J" not in name)
'''
# TODO: Identity operator (is)
'''
a = [1,2]
print("Id of a is: ",id(a))

b = [1,2]
print("Id of b is: ",id(b))

print(a is b)

c = b
print("Id of c is: ",id(c))
print(c is b)

'''

