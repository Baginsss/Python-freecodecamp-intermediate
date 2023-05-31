# Itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat

# product: Cartesian product of input iterables
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

# permutations: r-length tuples, all possible orderings, no repeated elements
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

perm = permutations(a, 2) # r = 2
print(list(perm))

# combinations: r-length tuples, in sorted order, no repeated elements

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# accumulate: returns accumulated sums (or other binary function results)
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

# groupby: returns iterator of key and grouped iterator

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

# count: returns iterator that counts up infinitely from a value
for i in count(10):
    print(i)
    if i == 15:
        break

# cycle: returns iterator that cycles through an iterator infinitely
a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break

# repeat: returns iterator that repeats an object infinitely or up to a limit
for i in repeat(1, 4):
    print(i)