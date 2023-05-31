# Errors and Exceptions

a = 10
# print(a))
# exception error

# a = 5 + '10'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# import somemodule
# ModuleNotFoundError: No module named 'somemodule'

a = 5
# b = c
# NameError: name 'c' is not defined

# f = open('somefile.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt

# a = [1, 2, 3]
# a.remove(4)
# ValueError: list.remove(x): x not in list

mydict = {'name': 'Max'}
# mydict['age']
# KeyError: 'age'

x = -5
if x < 0:
    raise Exception('x should be positive')

assert (x >= 0), 'x is not positive'

try:
    a = 10 / 0
except:
    print('some error occurred')

try: 
    a = 10 / 0
except Exception as e:
    print(e)

class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

try:    
    test_value(200)
except ValueTooHighError as e:
    print(e)

