'''
async programming 
Async programming in Python is a programming paradigm that allows you to write 
asynchronous, non-blocking code to handle I/O-bound operations more efficiently.
It enables you to perform multiple tasks concurrently without blocking the execution
of the main program or waiting for each operation to complete before moving on to the next one.

Python provides an asyncio library in the standard library
that supports asynchronous programming using coroutines, which are special functions
that can be paused and resumed during execution. These coroutines are defined using
the async def syntax
and use the await keyword to pause the execution until the awaited task completes.

'''

import asyncio

async def greet(name):
     print(f"Hello, {name}!")
     await asyncio.sleep(1)  # Simulate some I/O-bound operation
     print(f"Goodbye, {name}!")

async def main():
     await asyncio.gather(
         greet("Alice"),
         greet("Bob"),
         greet("Charlie")
     )

asyncio.run(main())



async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)  # Simulate an asynchronous operation (non-blocking sleep)

async def print_letters():
    for letter in 'ABCDE':
        print(letter)
        await asyncio.sleep(0.5)  # Simulate another asynchronous operation

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())

    await task1
    await task2

asyncio.run(main())
