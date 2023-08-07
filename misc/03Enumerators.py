'''
enumerate 

enumerate(iterable, start=0)
iterable: The sequence you want to iterate over, such as a list, tuple, or string.
start (optional): The index from which counting starts. By default, it is set to 0.

'''

fruits = ["banana", "mango", "apple", "orange", "guava"]

for idx, item in enumerate(fruits):
    print(f"fruit at index {idx} is {item}")