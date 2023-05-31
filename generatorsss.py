def mygenerator():
    yield 1
    yield 2
    yield 3 # yield is a keyword that is used like return, except the function will return a generator

g = mygenerator()
print(g)
print(next(g))

for i in g:
    print(i)



def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(firstn(10))
print(sum(firstn(10)))

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(firstn_generator(10))
print(sum(firstn_generator(10)))

import sys

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
print(fib)

for i in fib:
    print(i)

mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)
