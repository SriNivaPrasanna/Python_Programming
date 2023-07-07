'''
lists -> [ ]
list()
mutable -> it can be changed
iterable -> we can loop over it
indexed -> Each value in the list can be fetch using the index number
'''

fruits = ["mango", "pineapple", "apple", "guava", "orange"]
#print("len of fruits: ", len(fruits))
#print(fruits)
#print(type(fruits))

#fruits[1] = "apple"
#print(fruits)


# TODO: iteration
#for f in fruits:
#  print(f)

#for i in range(len(fruits)):
#    print(f'fruit at index : {i} is {fruits[i]}')

#i = 0
#  while i < len(fruits):
#      print(fruits[i])
#      i += 1

# TODO: indexing
#print(fruits[0])
#print(fruits[1])

#print(fruits[-1])

# TODO: slicing
# list_name[start_index : end_index : step]
# start_index is inclusive
# end_index is exclusive

# print(fruits[ : : ])
# print(fruits[ : : -1])

# print(fruits[1 : 4])
#print(fruits[-4 : -1])

# print(fruits[0 : 5 : 2])
# print(fruits[ : : 2])

# TODO: append -> adds element at the end
# print("Before: ",fruits)
# fruits.append("grapes")
# print("after: ", fruits)

# TODO: dynamically a user input list
# size = int(input("enter the size of the list: "))
# val = []

# for i in range(size):
#     ele = int(input("Enter the num: "))
#     val.append(ele)
# else:
#     print("list is: ",val)

# print("fruits count is: ",fruits.count("guava"))

# print(fruits.index("mango"))
# print(fruits.index("orange" , 1 , 3))

#fruits.clear()
#print(fruits)

#l1=[ ]
#l2=list()
#print(l1)  #[ ]
#print(l2)  #[ ]

#arr = ["a", "b", "c", 4, 7]
#print(arr)  
#print(type(arr))

#myList = list ((1,2,3,4,5))
#print(myList)  
#print(type(myList))

#arr = ["a", "b", "c", "d", "e"]
#print(arr) 
#print(type(arr))
#for i in arr:
#    print(i)

#arr = ["a", "b", "c", "d", "e"]

#for i in range(len(arr)):
    # accessing the value using index value
#    print(i , arr[i])

#fruits=["apple","kiwi","banana","mango"]
#print("fruit at index 0: ",fruits[0])
#print("fruit at index 1: ",fruits[1])
#print("fruit at index 2: ",fruits[2])
#print("fruit at index 3: ",fruits[3])

## Negative Indexing
#print("fruit at index -1: ",fruits[-1])
#print("fruit at index -2: ",fruits[-2])
#print("fruit at index -3: ",fruits[-3])
#print("fruit at index -4: ",fruits[-4])

# Modifying a list
#fruits=["apple","kiwi","banana","mango"]
#print("Original List")
#print(fruits)
#fruits[0]="guava"
#print("Updated List:")
#print(fruits)

# slicing
#fruits=["apple","kiwi","banana","mango"]
#print(fruits[0:2])
#num=[1,2,3,4,5,6,7,8]
# It will print all odd numbers as it will skip one element as space=2
#print(num[0:8:2])

# It will provide multiples of 3 as space is 3 
#print(num[2:8:3])

# slicing from backwards
#print(num[-4:-1])

#fruits=["apple","kiwi","banana","mango"]
#fruits.append("pineapple")
#print(fruits)
#  ['apple', 'kiwi', 'banana', 'mango', 'pineapple']

#fruits=["apple","kiwi","banana","mango"]
#fruits.insert(2,"guava")
#print(fruits)

#  ['apple', 'kiwi', 'guava', 'banana', 'mango']


#fruits=["apple","kiwi","banana","mango"]
#more_fruits=["litchi","watermelon","plum"]
#fruits.extend(more_fruits)
#print(fruits)
#['apple', 'kiwi', 'banana', 'mango', 'litchi', 'watermelon', 'plum']

#fruits=["apple","kiwi","banana","mango"]
#print(fruits.index("kiwi"))  #1

#print(fruits.index("tomato"))

#fruits=["apple","kiwi","banana","mango"]
#fruits.remove("apple")
#print(fruits)

#fruits=["apple","kiwi","banana","mango"]
#fruits.sort()
#print(fruits)
#  ['apple', 'banana', 'kiwi', 'mango']
#fruits.sort(reverse=True)
#print(fruits)
#  ['mango', 'kiwi', 'banana', 'apple']

#fruits=["apple","kiwi","banana","mango"]
#fruits.reverse()
#print(fruits)
# ['mango', 'banana', 'kiwi', 'apple']

#fruits=["apple","kiwi","banana","mango"]
#print(fruits.pop())

#  'mango'

#print(fruits)
# ['apple', 'kiwi', 'banana']

#print(fruits.pop(2))
#  'banana'

#print(fruits)
#  ['apple', 'kiwi']


#fruits=["apple","kiwi","banana","mango","apple","apple"]
#print(fruits.count("apple"))  #3
#print(fruits.count("kiwi"))  #1

#newList = [ expression(element) for element in oldList if condition ]

# to make a list of squares
#l=[i*i for i in range(1,11)]
#print(l)
#  [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

#num="10,20,30,40,50"
#numbers=[int(no) for no in num.split(',')]
#print(numbers)
#[10, 20, 30, 40, 50]

#creating a list containing even values
#list = [i for i in range(11) if i % 2 == 0]
#print(list)
#[0, 2, 4, 6, 8, 10]

#list = [i for i in range(11) if i % 2 != 0]
#print(list)
#[1, 3, 5, 7, 9]

#lis = [i**2 if i % 2 == 0 else i**3 for i in range(5)]
#print(lis)
#[0, 1, 4, 27, 16]
#lis = [i**2 if i % 2 != 0 else i**3 for i in range(5)]
#print(lis)
#[0, 1, 8, 9, 64]


# TODO: index(element, start, end)
fruits = ["mango", "pineapple", "apple", "guava", "orange"]
#print(fruits.index("apple"))

# TODO: Will be giving error as we are searching after 3rd index
#print(fruits.index("apple", 3))

#fruits.insert( 2, "plum")
#print(fruits)

#print("BEFORE: ", fruits)
#fruits.remove("apple")
#print("AFTER: ", fruits)

# TODO: reversing the entire list
#print("BEFORE: ", fruits)
#fruits.reverse()
#print("AFTER: ", fruits)

# TODO: sort 
#print("BEFORE: ", fruits)
# # ascending order
#fruits.sort()
# # TODO: descending order
#fruits.sort(reverse=True)
#print("AFTER: ", fruits)

#print(sorted(fruits))
#fruits = sorted(fruits)
#print(fruits)
'''
# TODO: copy

fruits1 = fruits.copy()
fruits[0] = "pear"
print("Fruits: ", fruits)
print("Fruits1: ", fruits1)
'''
import copy

list1 = [ 1, [2, 3] , 4 ]
list2 = list1
list4 = copy.deepcopy(list1)

list1.append(5)
list1[1][1] = 999

print("List 1: ",list1)
print("List 2: ",list2)

print([1,2,3] + [5,6])
print([1,2,3] * 2)