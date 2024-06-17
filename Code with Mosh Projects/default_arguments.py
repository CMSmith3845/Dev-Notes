def increment(number, by=1):
    return number + by


print(increment(2))  # This would output 3 because the value of the 2nd argument is defined in the parameters

print(increment(2, 5))  # This will output 7 because the value of by was defined in this statement.

# Generally the arguments of a function are required but this is a way to make them optional and define them later.
# All optional parameters should come after the required ones, otherwise the code won't work i.e.
# def increment(number, by=1, another) this code will not work it must have the by=1 as the last parameter
