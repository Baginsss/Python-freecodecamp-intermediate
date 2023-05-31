# Sets: unordered, mutable, no duplicates

myset = set("Hello")
print(myset)

myset = set()

myset.add(1) 
myset.add(2)
myset.add(3)

print(myset)

myset.remove(3)
print(myset)

myset.discard(2)
print(myset)

myset.clear()
print(myset)

# myset.pop()

myset = {1, 2, 3, 4, 5, 6}
for i in myset:
    print(i)

if 1 in myset:
    print("yes")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

# union will combine the two sets and remove duplicates

i = odds.intersection(primes)
print(i)

# intersection will return the values that are in both sets

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

# difference will return the values that are in setA but not in setB

diff = setA.symmetric_difference(setB)
print(diff)

# symmetric_difference will return the values that are in setA or setB but not both

setA.update(setB)
print(setA)


setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.intersection_update(setB)
print(setA)

setA.symmetric_difference_update(setB)
print(setA)

# symetric_difference_update will update setA with the values that are in setA or setB but not both

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setB.issubset(setA))

# subset will return true if setB is a subset of setA

print(setA.issuperset(setB))

# superset will return true if setA is a superset of setB

a = frozenset([1, 2, 3, 4])

# frozenset is an immutable set

# a.add(5)
# a.remove(3)
# this will throw an error because frozenset is immutable


