'''
tuples -> ()
tuple()

iterable , ordered , immutable
'''

#fruits = ("mango", "apple", "banana", "papaya", "grapes", "guava")
'''
print(fruits)
print(type(fruits))

for i in fruits:
   print(i)

print(fruits[0])
print(fruits[-1])

fruits[0] = "orange"
print(fruits)
'''
# TODO: slicing
fruits = ("mango", "pineapple", "apple", "guava", "orange")
print(fruits[ : : -1])

print(fruits[ 2 : 4 ])

print(fruits.count("mango"))

print(fruits.index("mango"))
'''
print( (1, 2) + (3, 4))

tup = ( [1, 2] , [3, 4] )
print(tup)
print(type(tup))
print(tup[0][1])
print(tup[1][1])
tup[0][1] = 5
tup[1][1] = 10
print(tup)

tup = (1, 2, 3)
print(tup.__sizeof__())

li = [1, 2, 3]
print(li.__sizeof__())
'''
'''
# tuple in python
t=()
t1=tuple()
print(t)
print(t1)
#()
#()
# Concat Tuple
t1=(1,2,3,4,5)
t2=(6,7,8)
print(t1+t2)
print(type(t1+t2))
#  (1, 2, 3, 4, 5, 6, 7, 8)
#<class 'tuple'>
'''
'''
# Nesting
t=((1,2,3,4),(5,6,0,7))
print(t)  # ((1, 2, 3, 4), (5, 6, 0, 7))
print(t[0])  # (1, 2, 3, 4)
print(t[0][1])  # 2

t=("python",)*3
print(t)
#  ('python', 'python', 'python')
'''
'''
#Indexing value
t=(1,2,3,5,6)
t[4]=86
print(t)
Traceback (most recent call last):
  File "C:\Python_9PM\02inbuilds\02Tuples.py", line 74, in <module>
    t[4]=86
    ~^^^
TypeError: 'tuple' object does not support item assignment
'''
'''
#deleting a tuple
t=(1,2,3,5,6)
del t
print(t)
Traceback (most recent call last):
  File "C:\Python_9PM\02inbuilds\02Tuples.py", line 86, in <module>
    print(t)
          ^
NameError: name 't' is not defined
'''
'''
t=(1,2,3,5,6)

# length of a tuple
length=len(t)
print("length is ",length)  # length is  5

# max of a tuple
maximum=max(t)
print("maximum is ",maximum)  # maximum is  6

# min of a tuple
minimum=min(t)
print("minimum is ",minimum)  # minimum is  1

# converting list into a tuple
l=[1,2,3,4,5]
t=tuple(l)
print(type(t))  #  <class 'tuple'>
print(t)  # (1, 2, 3, 4, 5)
# converting tuple into a list
l=(1,2,3,4,5)
t=list(l)
print(type(t))  #  <class 'list'>
print(t)  # [1, 2, 3, 4, 5]
'''