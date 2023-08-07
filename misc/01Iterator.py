'''
In Python, an iterator is an object that allows you to traverse through a sequence of elements, 
one at a time, without having to know the underlying data structure or implementation details. 
It provides a common interface for iterating over various types of collections such as 
lists, tuples, dictionaries, and custom-defined objects.

The iterator protocol in Python consists of two methods:

__iter__: This method returns the iterator object itself and is required for an object to be considered an iterator.

__next__: This method returns the next element in the sequence. When there are no more elements to be returned, it raises the StopIteration exception to signal the end of iteration.
'''

st = "Python"
it = iter(st)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



iterable = (1, 2, 3, 4)
iterator_obj = iter(iterable)

for item in iterator_obj:
        print(item, end=",")

print(next(iterator_obj))

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            element = self.data[self.index]
            self.index += 1
            return element
        else:
            raise StopIteration
    
my_list = [1,2,3,4,5]
my_iterator = MyIterator(my_list)

#Method1
for item in my_iterator:
     print(item)

#Method2
my_iter = iter(my_iterator)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

