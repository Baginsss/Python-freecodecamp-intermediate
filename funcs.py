"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)
"""

def print_name(name):
    print(name)

print_name('Alex')

def fool(a, b, c):
    print(a, b, c)

fool(c=1, b=2, a=3)

fool(1, b=2, c=3)

def fool(a, b, c, d=4):
    print(a, b, c, d)

fool(1, b=2, c=3)

def fool(a, b, c, *args, **kwargs):
    print(a, b, c)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

# args and kwargs arguments can take any number of arguments

fool(1, 2, 3, 4, 5, six=6, seven=7)

def fool(a, b, *, c, d):
    print(a, b, c, d)

fool(1, 2, c=3, d=4)

def fool(*args, last):
    for arg in args:
        print(arg)
    print(last)

fool(1, 2, 3, last=200)

# unpacking arguments

def fool(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
fool(*my_list)

dictonary1 = {'a': 1, 'b': 2, 'c': 3}
fool(**dictonary1)

def fool():
    x = number
    print('number inside function:', x)

number = 0
fool()

def fool():
    x = 3
    print('number inside function:', x)

fool()

def fool():
    global number
    number = 3

number = 0
fool()
print(number)
# I think it's not working as intended ;/

def fool(list1):
    list1.append(4)

my_list = [1, 2, 3]
fool(my_list)
print(my_list)

def fool(a_list):
    a_list = [200, 300, 400]
    a_list.append(4)
    a_list[0] = -100

my_list = [1, 2, 3]
fool(my_list)
print(my_list)
# Now it is suppoused not to work as intended