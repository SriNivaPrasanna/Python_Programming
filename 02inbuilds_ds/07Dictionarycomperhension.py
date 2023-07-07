d = {i : i**2 for i in range(5)}
#print(d)

d = {i : i**3 for i in range(5)}
#print(d)

# TODO: using if
# list of evens
even = {i : i for i in range(10) if i%2 == 0}
#print(even)
odd = {i: i for i in range(10) if i%2 != 0}
#print(odd)

# TODO: using if and else
nums = {i:(i**2) if i%2 ==0 else i**3 for i in range(10)}
print(nums)

nums = {i: even if i%2 ==0 else odd for i in range(10)}
print(nums)


