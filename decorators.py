# Decorators are functions that take another function as an argument, add some kind of functionality, and then return another function. All of this without altering the source code of the original function that we passed in.

import functools
from typing import Any

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def print_name():
    print("Mateusz")

print_name()

@start_end_decorator
def add5(x):
    return x + 5

add5(10)

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times = 3)
def greet(name):
    print(f"Hello {name}")

greet("Mateusz")

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_rep = [repr(a) for a in args] # repr() returns a printable representation of the given object
        kwargs_rep = [f"{k}={v!r}" for k, v in kwargs.items()] # !r calls repr() on the argument
        signature = ", ".join(args_rep + kwargs_rep) # join() returns a string in which the string elements of sequence have been joined by str separator
        print(f"Calling {func.__name__}({signature})") # __name__ is a special attribute of every function
        result = func(*args, **kwargs) # func is the function that we passed in
        print(f"{func.__name__!r} returned {result!r}") # !r calls repr() on the argument
        return result
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

say_hello("Mateusz")

# class decorators

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwds):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwds)


@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()
