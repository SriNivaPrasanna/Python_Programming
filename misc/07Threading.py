import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)  # Simulate some work (blocking sleep)

def print_letters():
    for letter in 'ABCDEFGHIJ':
        print(letter)
        time.sleep(0.5)  # Simulate some other work

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("All threads have finished.")