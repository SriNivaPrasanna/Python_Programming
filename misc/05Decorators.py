'''
DECORATORS: 

In Python, decorators are a powerful concept that allows you to
modify or extend the behavior of functions or methods without changing their code directly. 
Decorators are higher-order functions, which means they take another function as an argument and return a new function.
They are denoted by the @decorator_name syntax and are placed just above the function definition.

Decorators are often used for tasks such as 
logging, authentication, memoization, and other cross-cutting concerns that apply to multiple functions. 
They provide a clean and reusable way to add functionality to functions dynamically.

'''

def my_decorator(func):
    def wrapper():
        print("*******************")
        func()
        print("********************")
    return wrapper 
#Method 1
@my_decorator
def say_hello():
    print("Hello")

say_hello()

#Method 2
def say_hello():
    print("Hello")
decorated_func = my_decorator(say_hello)
decorated_func()


def repeat(no_of_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(no_of_times):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator

@repeat(no_of_times=3)
def say_hi(name):
    print("HI! ",name)

say_hi("JANE")
