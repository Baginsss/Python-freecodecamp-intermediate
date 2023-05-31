import random
random.seed(1) # seed is used to generate the same random numbers every time

a = random.random()
print(a)

b = random.uniform(1, 10)
print(b)

c = random.randint(1, 10)
print(c)

d = random.normalvariate(0, 1) # mean 0, standard deviation 1, might be useful for working in statistics
print(d)

mylist = list("ABCDEFGH")
e = random.choice(mylist)
print(e)

e = random.choices(mylist, k=3) # k is the number of choices
print(e)

random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)

import secrets
# secrets is used for cryptography, it takes more time for those algorithms to generate random numbers, and only has three functions

a = secrets.randbelow(10) # 0-9
print(a)

b = secrets.randbits(4) # 4 bits, 0-15
print(b)

mylist = list("ABCDEFGH")
c = secrets.choice(mylist)
print(c)

import numpy as np
# numpy is a library for scientific computing, it has a random module

a = np.random.rand(3) # 3 random numbers between 0 and 1
print(a)

b = np.random.rand(3, 3) # 3x3 matrix
print(b)

c = np.random.randint(0, 10, 3) # 3 random integers between 0 and 9
print(c)

d = np.random.randint(0, 10, (3, 3)) # 3x3 matrix
print(d)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr) # shuffle the array
print(arr)

np.random.seed(1)
print(np.random.rand(3))
np.random.seed(1)
print(np.random.rand(3))
