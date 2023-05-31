zeros = "AB" * 10
print(zeros)

def fool(a, b, *args, **kwargs):
    print(a)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
    
fool(1, 2, 3, 4, 5, six=6, seven=7)

def fool(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
fool(*my_list)

my_dictionary = {'a': 1, 'b': 2, 'c': 3}
fool(**my_dictionary)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

*beginning, last = numbers
print(beginning)
print(last)

