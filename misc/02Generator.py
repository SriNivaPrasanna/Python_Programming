'''
Generators in Python are a type of iterable, just like iterators, 
but they are defined using functions with a special syntax. 
Instead of using the __iter__() and __next__() methods as in custom iterators, 
generators use the yield keyword to produce a series of values during iteration.
The main advantage of generators over regular iterators 
is that they allow you to create iterators in a more concise and memory-efficient manner.

The main benefits of using generators include:

Memory efficiency: Generators produce elements one at a time, on-the-fly, without storing the entire sequence in memory. This is especially useful when dealing with large datasets.

Lazy evaluation: Generators use lazy evaluation, meaning they produce values only when requested. This allows you to work with infinite sequences or processes without running into memory issues.

Simplicity and readability: Generator functions tend to be more concise and easier to read compared to writing custom iterator classes.
'''

def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1

# Using the generator
my_generator = count_up_to(5)

#for num in my_generator:
  #   print(num)

my_generator = (x * 3 for x in range(6))

for num in my_generator:
    print(num)