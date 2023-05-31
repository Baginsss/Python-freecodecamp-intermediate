org = 5
cpy = org
cpy = 6

print(org)
print(cpy)

import copy
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
cpy[0] = -10
print(cpy)
print(org)

org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Bob', 23)
p2 = copy.copy(p1)
p2.age = 20
print(p1.age)
print(p2.age)

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

Company = Company(p1, p2)
Company_clone = copy.copy(Company)
Company_clone.boss.age = 50
print(Company_clone.boss.age)
print(Company.boss.age)

