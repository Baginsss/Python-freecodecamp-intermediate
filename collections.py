# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
a = "aaaaabbbbbccccccdddddd"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

# Namedtuple
Point = namedtuple('Point', 'x,y')

pt = Point(1, -4)

print(pt)

# OrderedDict
ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5

print(ordered_dict)

# Defaultdict
d = defaultdict(int)

d['a'] = 1
d['b'] = 2

print(d['c'])

# Deque
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)

print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([4, 5, 6])
print(d)

d.extendleft([7, 8, 9])
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)

