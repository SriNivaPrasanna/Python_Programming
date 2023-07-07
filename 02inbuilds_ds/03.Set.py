'''
sets -> collection of particular category
set()
{}
No indexing : these do not have any fixed position
iterable
IT doesnot have the duplicate values
'''

a = {1,2,3,45,65,3}
#print(a)
#print(type(a))
#a.add(55)
#print(a)

# TODO: if that particular element do not exist , it will not throw any error
#a.discard(3)
#print(a)

# TODO: if that particular element do not exist , it gives KeyError
#a.remove(31)

'''
a = {1,2,3,4}
b= {3,4,5,6}

# TODO: Union
print(a.union(b))
print(a | b)

# TODO: intersection
print(a.intersection(b))
print(a & b)

# TODO: difference
print(a.difference(b))
print(a - b)
print(b.difference(a))
print(b - a)
'''

#l=[1,2,3,4,52,1,2,5]
#s=set(l)
#print(s) 
# {1, 2, 3, 4, 5, 52}
# TODO : its shows TypeERROR
#s={1,2,3,4,5,6}
#print(s[3])

my_list = ['a', 'b', 'c', 'd']
frozen_set = frozenset(my_list)
print(frozen_set)

# frozenset({'b', 'c', 'd', 'a'})

# TODO : Iteration
s={1,2,3,4,5,6}
for i in s:
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6

#Add Element 
'''
s={1,2,3,4,5,6}
s.add(7)
print("after adding 7",s)

s.update([25,75])
print(s)
'''
'''

s={1,2,3,4,5,6}
# pops out element from front
s.pop()
print("after using pop function: ",s)

#output
# after using pop function:  {2, 3, 4, 5, 6}

# doesnot gives error if element is not present
s.discard(5)
print(s)
# remove function gives key error if element is not present
#s.remove(15) #will through KeyError

'''
s1={1,2,3,4,5}
s2={3,4,6,76,85,5}

# intersection
print("intersection: ",s1.intersection(s2))
print("intersection: ",s1&s2)

# union
print("union: ",s1.union(s2))
print("union: ",s1|s2)

# set difference
print("s1-s2",s1-s2)
print("s1-s2",s1.difference(s2))

print("s2-s1",s2-s1)

# to check s1 is subset of s2
print('issubset: ',s1<=s2)

# clear the set
s1.clear()
s2.clear()
print(s1)
print(s2)
