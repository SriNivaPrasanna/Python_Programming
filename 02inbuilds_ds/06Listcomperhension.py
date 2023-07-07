'''
List comprehension
'''
l = []
for i in range(5):
  l.append(i)

#print(l)

l = [i for i in range(5)]
#print(l)

s

even = [i for i in range(10) if i%2 == 0]
#print(even)
odd = [i for i in range(10) if i%2 != 0]
#print(odd)

# TODO: using if and else
nums = [(i**2) if i%2 ==0 else i**3 for i in range(10)]
#print(nums)

nums = [even if i%2 ==0 else odd for i in range(10)]
#print(nums)

#nums= [even if i%2 ==0 ((i**2) if i%2 ==0 else (i**3)) else odd ((i**2) if i%2 ==0 else i**3) for i in range(10)]
#print(nums)