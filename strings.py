# Strings: ordered, immutable, text representation
my_string = "I'm a programmer"
print(my_string)

char = my_string[0]
print(char)

substring = my_string[1:5]
print(substring)

substring = my_string[::-1]
print(substring)

greeting = "Hello"
name = "Matt"
sentence = greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if "ell" in greeting:
    print("yes")
else:
    print("no")

my_string = "    Hello World    "
print(my_string)

my_string = my_string.strip()
print(my_string)

print(my_string.upper())
print(my_string.lower())

print(my_string.startswith("He"))
print(my_string.endswith("ld"))

print(my_string.find("o"))

print(my_string.replace("World", "Universe"))

my_string = "how are you doing"
my_list = my_string.split()
print(my_list)

new_string = " ".join(my_list)
print(new_string)

my_list = ["a"] * 6
print(my_list)

#Bad
my_string = ''
for i in my_list:
    my_string += i
print(my_string)

#Good
my_string = ''.join(my_list)
print(my_string)

from timeit import default_timer as timer

my_list = ["a"] * 1000000

start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)

start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)

#Formatting strings
#%, .format, f-Strings

var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 3.123456
my_string = "the variable is %.2f" % var
print(my_string)

var = 3.123456
my_string = "the variable is {:.2f}".format(var)
print(my_string)

#f-Strings: are faster than .format and %

var = 3.123456
var2 = 6
my_string = f"variable is {var} and {var2}"
print(my_string)

