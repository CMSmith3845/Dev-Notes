print(type(5))  # This will return that "5" is an integer
print(type(range(5)))  # This will return that the range(5) is a range, which is a complex type of data

# This complex data type is iterable, which means it can be iterated over or used in a for loop.
# definition of iterable is something that be looped or used over and over again
for x in range(5):  # This means that x is iterated 5 times and each time it will return a different value.
    print(x)  # note this iteration stops at 4 not 5

for x in "Python":  # Strings are also iterable, this will print x as each character on a new line
    print(x)

for x in [1, 2, 3, 4, "Python"]:  # Lists are also iterable, this will print each number and the word python on new line
    print(x)

for item in shopping_cart:  # shopping_cart is custom object we make, you can make it iterable, so it will print each
    print(item)  # each item that is contained within the custom object shopping_cart
